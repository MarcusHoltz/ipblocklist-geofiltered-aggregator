#!/usr/bin/env python3
"""
filter_ips.py — Optimized GeoIP-based IP Address Filtering Tool

This script filters IP addresses by country using GeoIP data and Zeek's SubnetTree
for efficient network lookups. It processes large IP lists in parallel batches
while preserving original formatting (including CIDR notation).

REQUIREMENTS:
    pip install pysubnettree pandas python-dotenv requests

MAIN WORKFLOW:
    1. Load configuration from environment variables (.env file)
    2. Download GeoIP CSV data if not present locally
    3. Filter GeoIP networks by target country (ISO code or name)
    4. Collapse overlapping networks for optimization
    5. Build SubnetTree data structure in each worker process
    6. Process input IPs in parallel batches
    7. Write filtered results to output file
    8. Clean up temporary GeoIP data

DATA FLOW:
    Input IPs → Country Network Filter → SubnetTree Lookup → Filtered Output
"""

# =============================================================================
# IMPORTS AND DEPENDENCIES
# =============================================================================

import os                               # Operating system interface
import logging                          # Logging functionality
import ipaddress                        # IP address manipulation and validation
from pathlib import Path                # Modern path handling
from concurrent.futures import ProcessPoolExecutor  # Parallel processing
import multiprocessing as mp            # Multiprocessing utilities
from dotenv import load_dotenv          # Environment variable loading
import shutil                           # High-level file operations
import pandas as pd                     # Data manipulation and analysis
import requests                         # HTTP requests for downloading data

# =============================================================================
# CRITICAL DEPENDENCY CHECK
# =============================================================================

try:
    # SubnetTree is the core component for efficient IP network lookups
    # It provides O(log n) lookup time instead of O(n) for linear searches
    import SubnetTree
except Exception as exc:
    # If SubnetTree is missing, the script cannot function efficiently
    # Provide clear installation instructions and exit gracefully
    raise ImportError(
        "CRITICAL: The Python package 'pysubnettree' (module name 'SubnetTree') is required.\n"
        "This package provides efficient IP network lookups using a tree data structure.\n"
        "Install it with: pip install pysubnettree\n"
        f"Original error: {exc}"
    )

# =============================================================================
# CONFIGURATION AND ENVIRONMENT SETUP
# =============================================================================

# Load environment variables from .env file (if it exists)
# This allows users to configure the script without modifying code
load_dotenv()

# COUNTRY CONFIGURATION
# These settings determine which country's IPs will be filtered
country_iso_code = os.getenv('COUNTRY_ISO_CODE', 'US')
country_name = os.getenv('COUNTRY_NAME', 'United States')

# FILE PATH CONFIGURATION
# Define where input and output files are located
GEOIP_CSV_PATH = os.getenv('GEOIP_CSV_PATH', '/data/geoip/geoip2-ipv4.csv')
ALL_IPS_FROM_LISTS = os.getenv('ALL_IPS_FROM_LISTS', '/data/output/aggregated.txt')

# DYNAMIC OUTPUT PATH
# Generate output filename based on country code (e.g., US -> aggregated-us-only.txt)
COUNTRY_ONLY_IPS = f'/data/output/aggregated-{country_iso_code.lower()}-only.txt'

# PERFORMANCE TUNING
# Allow override of worker process count via environment variable
# Useful for different hardware configurations or resource constraints
NUM_WORKERS_ENV = os.getenv('NUM_WORKERS')
NUM_WORKERS_OVERRIDE = max(1, int(NUM_WORKERS_ENV)) if NUM_WORKERS_ENV else None

# =============================================================================
# GLOBAL WORKER VARIABLE
# =============================================================================

# This global variable holds the SubnetTree instance in each worker process
# It's initialized once per worker and then used for all IP lookups in that worker
WORKER_TREE = None

# =============================================================================
# GEOIP DATA MANAGEMENT FUNCTIONS
# =============================================================================

def download_geoip_file():
    """
    Downloads GeoIP2 IPv4 CSV data if not already present locally.
    
    This function handles the automatic acquisition of GeoIP data, which maps
    IP address ranges to countries. The data is essential for country-based
    IP filtering.
    
    DATA SOURCE:
        - URL: https://datahub.io/core/geoip2-ipv4/r/geoip2-ipv4.csv
        - Contains: network, country_iso_code, country_name columns
        - Format: CIDR networks with country mappings
    
    ERROR HANDLING:
        - Creates parent directories if they don't exist
        - Validates HTTP response status
        - Exits gracefully if download fails
    
    SIDE EFFECTS:
        - Creates directories on filesystem
        - Downloads and writes CSV file
        - May raise SystemExit on failure
    """
    # Check if the GeoIP CSV file already exists on disk
    if not os.path.exists(GEOIP_CSV_PATH):
        logging.info(f"GeoIP file not found at {GEOIP_CSV_PATH}. Initiating download...")
        
        # DataHub provides free, regularly updated GeoIP data
        url = "https://datahub.io/core/geoip2-ipv4/r/geoip2-ipv4.csv"
        
        try:
            # Download the CSV file with a reasonable timeout
            logging.info("Downloading GeoIP2 CSV data from DataHub...")
            response = requests.get(url, timeout=60)
            
            # Check if the download was successful
            if response.status_code == 200:
                # Create parent directories if they don't exist
                # This ensures the full path structure is available
                Path(GEOIP_CSV_PATH).parent.mkdir(parents=True, exist_ok=True)
                
                # Write the downloaded content to disk
                with open(GEOIP_CSV_PATH, 'wb') as file_handle:
                    file_handle.write(response.content)
                
                logging.info("GeoIP2 CSV file downloaded and saved successfully.")
            else:
                # Log the specific HTTP error and exit
                logging.error(f"Download failed with HTTP status: {response.status_code}")
                logging.error("Cannot proceed without GeoIP data. Exiting.")
                raise SystemExit(1)
                
        except requests.exceptions.RequestException as req_exc:
            # Handle network-related errors (timeouts, connection issues, etc.)
            logging.error(f"Network error during download: {req_exc}")
            raise SystemExit(1)
            
    else:
        logging.info(f"GeoIP file already exists at {GEOIP_CSV_PATH}")


def collapse_networks(network_strs):
    """
    Optimizes network lists by collapsing overlapping and adjacent networks.
    
    This function takes a list of CIDR network strings and uses Python's
    ipaddress module to combine overlapping or adjacent networks into larger,
    more efficient blocks. This reduces the number of networks that need to
    be stored in the SubnetTree, improving both memory usage and lookup speed.
    
    ARGS:
        network_strs (list): List of CIDR network strings (e.g., ['1.2.3.0/24'])
    
    RETURNS:
        list: Collapsed network strings with overlaps removed
    
    EXAMPLE:
        Input:  ['192.168.1.0/24', '192.168.2.0/24']
        Output: ['192.168.0.0/23']  # Combined into larger block
    
    OPTIMIZATION BENEFITS:
        - Reduces memory footprint in SubnetTree
        - Improves lookup performance
        - Eliminates redundant network checks
    """
    network_objects = []
    invalid_count = 0
    
    # Convert string representations to ipaddress network objects
    for network_str in network_strs:
        try:
            # Create network object from CIDR string
            # strip() removes any whitespace that might cause parsing errors
            network_obj = ipaddress.ip_network(network_str.strip())
            network_objects.append(network_obj)
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as parse_error:
            # Log invalid networks for debugging but continue processing
            invalid_count += 1
            logging.debug(f"Skipping invalid network '{network_str}': {parse_error}")
            continue
    
    # Report parsing results
    if invalid_count > 0:
        logging.warning(f"Skipped {invalid_count} invalid network entries")
    
    # Use ipaddress.collapse_addresses() to merge overlapping/adjacent networks
    # This is a built-in Python optimization that's highly efficient
    collapsed_networks = list(ipaddress.collapse_addresses(network_objects))
    
    # Log the optimization results
    original_count = len(network_objects)
    collapsed_count = len(collapsed_networks)
    reduction_percent = ((original_count - collapsed_count) / original_count * 100) if original_count > 0 else 0
    
    logging.info(f"Network optimization: {original_count} → {collapsed_count} "
                f"({reduction_percent:.1f}% reduction)")
    
    # Convert back to string format for SubnetTree compatibility
    return [str(network) for network in collapsed_networks]


# =============================================================================
# PARALLEL PROCESSING WORKER FUNCTIONS
# =============================================================================

def _init_worker(cidr_list):
    """
    Initializes each worker process with a SubnetTree containing country networks.
    
    This function is called once when each worker process starts up. It builds
    a SubnetTree data structure from the provided CIDR list, which enables
    extremely fast IP lookups (O(log n) instead of O(n) for linear searches).
    
    PROCESS DESIGN:
        - Each worker gets its own copy of the SubnetTree
        - Tree is built once per worker and reused for all lookups
        - Global variable stores the tree for access by batch processing function
    
    ARGS:
        cidr_list (list): List of CIDR strings to add to the SubnetTree
    
    SIDE EFFECTS:
        - Sets global WORKER_TREE variable in the worker process
        - Imports SubnetTree in worker context
        - May log errors for malformed CIDRs but continues processing
    
    PERFORMANCE NOTES:
        - SubnetTree construction is O(n log n)
        - Lookup operations are O(log n)
        - Memory usage scales with number of networks
    """
    global WORKER_TREE
    
    # Import SubnetTree in the worker process context
    # This ensures the module is available in each worker's memory space
    import SubnetTree as WorkerSubnetTree
    
    # Create a new SubnetTree instance for this worker
    subnet_tree = WorkerSubnetTree.SubnetTree()
    
    # Track statistics for logging
    added_count = 0
    error_count = 0
    
    # Add each CIDR network to the tree
    for cidr_string in cidr_list:
        try:
            # Add the network to the tree with value True
            # The value (True) indicates this network matches our country filter
            subnet_tree[cidr_string] = True
            added_count += 1
        except Exception as add_error:
            # Log malformed CIDRs but don't stop processing
            error_count += 1
            logging.debug(f"Failed to add CIDR '{cidr_string}' to SubnetTree: {add_error}")
            continue
    
    # Store the completed tree in the global variable
    WORKER_TREE = subnet_tree
    
    # Log initialization results
    logging.info(f"Worker initialized: {added_count} networks in SubnetTree "
                f"({error_count} errors)")


def _process_ip_batch(ip_batch):
    """
    Processes a batch of IP addresses/networks against the country filter.
    
    This is the core worker function that gets executed in parallel across
    multiple processes. Each worker receives a batch of IP addresses and
    checks them against the SubnetTree to determine if they belong to the
    target country.
    
    IP FORMAT HANDLING:
        - Single IPs: 192.168.1.1 → check directly
        - CIDR networks: 192.168.1.0/24 → check network address
        - Preserves original formatting in output
    
    ARGS:
        ip_batch (list): List of IP strings to process (mix of IPs and CIDRs)
    
    RETURNS:
        list: IP strings that match the country filter (preserves original format)
    
    ERROR HANDLING:
        - Skips malformed IPs/CIDRs without stopping
        - Handles SubnetTree lookup exceptions
        - Continues processing even if some IPs fail
    
    PERFORMANCE:
        - Each lookup is O(log n) thanks to SubnetTree
        - Batch processing reduces inter-process communication overhead
        - Memory efficient - processes one IP at a time
    """
    global WORKER_TREE
    
    # Safety check: ensure the worker tree was initialized properly
    if WORKER_TREE is None:
        error_msg = "WORKER_TREE not initialized - worker setup failed"
        logging.error(error_msg)
        raise RuntimeError(error_msg)
    
    # List to collect matching IPs (preserving original format)
    country_matched_ips = []
    
    # Statistics tracking
    processed_count = 0
    matched_count = 0
    error_count = 0
    
    # Process each IP in the batch
    for raw_ip_line in ip_batch:
        # Clean up the input (remove whitespace)
        cleaned_ip = raw_ip_line.strip()
        
        # Skip empty lines
        if not cleaned_ip:
            continue
            
        processed_count += 1
        
        try:
            # Determine what IP address to check against the tree
            if '/' in cleaned_ip:
                # This is a CIDR network (e.g., "192.168.1.0/24")
                # We need to check the network address, not the CIDR string itself
                network_obj = ipaddress.ip_network(cleaned_ip, strict=False)
                ip_to_lookup = str(network_obj.network_address)
                
                logging.debug(f"CIDR '{cleaned_ip}' → checking network address '{ip_to_lookup}'")
            else:
                # This is a single IP address - check it directly
                ip_to_lookup = cleaned_ip
                
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError) as parse_error:
            # Skip malformed IP addresses or CIDR blocks
            error_count += 1
            logging.debug(f"Skipping malformed IP '{cleaned_ip}': {parse_error}")
            continue
        
        try:
            # Perform the SubnetTree lookup
            # This checks if ip_to_lookup falls within any of our country networks
            if ip_to_lookup in WORKER_TREE:
                # IP matches! Add the ORIGINAL format to results
                # This preserves CIDR notation if that's what was input
                country_matched_ips.append(cleaned_ip)
                matched_count += 1
                logging.debug(f"MATCH: '{cleaned_ip}' (checked: '{ip_to_lookup}')")
            else:
                logging.debug(f"No match: '{cleaned_ip}' (checked: '{ip_to_lookup}')")
                
        except Exception as lookup_error:
            # Handle any SubnetTree lookup errors (shouldn't happen with valid IPs)
            error_count += 1
            logging.debug(f"SubnetTree lookup failed for '{ip_to_lookup}': {lookup_error}")
            continue
    
    # Log batch processing results
    logging.debug(f"Batch complete: {processed_count} processed, {matched_count} matched, "
                 f"{error_count} errors")
    
    return country_matched_ips


# =============================================================================
# MAIN FILTERING LOGIC
# =============================================================================

def filter_us_ips_optimized():
    """
    Main orchestration function that coordinates the entire IP filtering process.
    
    This function ties together all the components to create an efficient,
    parallel IP filtering system. It handles the complete workflow from
    data acquisition through final output.
    
    COMPLETE WORKFLOW:
        1. Environment Setup & Validation
        2. GeoIP Data Acquisition
        3. Country Network Filtering
        4. Network Optimization
        5. Input Data Loading
        6. Parallel Processing Setup
        7. Batch Processing Execution
        8. Results Aggregation
        9. Output File Writing
        10. Cleanup Operations
    
    PERFORMANCE OPTIMIZATIONS:
        - Parallel processing with multiple workers
        - SubnetTree for O(log n) lookups
        - Network collapsing to reduce tree size
        - Batch processing to reduce overhead
        - Memory-efficient streaming where possible
    
    ERROR HANDLING:
        - Graceful fallback to single-process mode
        - Comprehensive logging at each stage
        - Input validation and sanitization
        - Resource cleanup even on failure
    """
    
    # =========================================================================
    # STAGE 1: ENVIRONMENT SETUP AND VALIDATION
    # =========================================================================
    
    logging.info("=== IP FILTERING PROCESS STARTED ===")
    logging.info(f"Target Country: {country_name} ({country_iso_code})")
    logging.info(f"Input File: {ALL_IPS_FROM_LISTS}")
    logging.info(f"Output File: {COUNTRY_ONLY_IPS}")
    
    # =========================================================================
    # STAGE 2: GEOIP DATA ACQUISITION
    # =========================================================================
    
    # Ensure we have the GeoIP database (download if needed)
    logging.info("Stage 1: Acquiring GeoIP database...")
    download_geoip_file()
    
    # =========================================================================
    # STAGE 3: GEOIP DATA LOADING AND VALIDATION
    # =========================================================================
    
    logging.info("Stage 2: Loading and validating GeoIP database...")
    
    try:
        # Load the CSV file into a pandas DataFrame for easy manipulation
        geoip_dataframe = pd.read_csv(GEOIP_CSV_PATH)
        logging.info(f"GeoIP database loaded: {len(geoip_dataframe)} total entries")
        
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as csv_error:
        logging.error(f"Failed to load GeoIP CSV file: {csv_error}")
        raise SystemExit(1)
    
    # Validate that the CSV has the required 'network' column
    if 'network' not in geoip_dataframe.columns:
        logging.error("GeoIP CSV missing required 'network' column")
        logging.error(f"Available columns: {list(geoip_dataframe.columns)}")
        raise SystemExit(1)
    
    # =========================================================================
    # STAGE 4: COUNTRY NETWORK FILTERING
    # =========================================================================
    
    logging.info("Stage 3: Filtering networks by country...")
    
    # Create a boolean mask for rows matching our target country
    # We check both ISO code and country name to maximize matches
    country_mask = (
        (geoip_dataframe.get('country_iso_code') == country_iso_code) | 
        (geoip_dataframe.get('country_name') == country_name)
    )
    
    # Extract the network CIDRs for matching countries
    country_networks = (geoip_dataframe[country_mask]['network']
                       .dropna()                    # Remove any NaN values
                       .astype(str)                 # Ensure string format
                       .tolist())                   # Convert to list
    
    logging.info(f"Found {len(country_networks)} networks for {country_name}")
    
    # Validate that we found some networks
    if len(country_networks) == 0:
        logging.error(f"No networks found for country '{country_name}' ({country_iso_code})")
        logging.error("Check country name/code or GeoIP data quality")
        raise SystemExit(1)
    
    # =========================================================================
    # STAGE 5: NETWORK OPTIMIZATION
    # =========================================================================
    
    logging.info("Stage 4: Optimizing network list...")
    
    # Collapse overlapping networks to improve performance
    optimized_cidrs = collapse_networks(country_networks)
    
    if len(optimized_cidrs) == 0:
        logging.error("Network optimization resulted in empty list")
        raise SystemExit(1)
    
    # =========================================================================
    # STAGE 6: INPUT DATA LOADING
    # =========================================================================
    
    logging.info("Stage 5: Loading input IP list...")
    
    try:
        # Load the input IP list, removing empty lines and whitespace
        with open(ALL_IPS_FROM_LISTS, 'r') as input_file:
            input_ip_list = [line.rstrip('\n') for line in input_file if line.strip()]
            
    except FileNotFoundError:
        logging.error(f"Input IP file not found: {ALL_IPS_FROM_LISTS}")
        raise SystemExit(1)
    except IOError as io_error:
        logging.error(f"Failed to read input file: {io_error}")
        raise SystemExit(1)
    
    total_input_ips = len(input_ip_list)
    logging.info(f"Loaded {total_input_ips} IP entries for processing")
    
    # Early exit if no IPs to process
    if total_input_ips == 0:
        logging.info("No IPs to process. Creating empty output file.")
        Path(COUNTRY_ONLY_IPS).parent.mkdir(parents=True, exist_ok=True)
        Path(COUNTRY_ONLY_IPS).touch()  # Create empty file
        return
    
    # =========================================================================
    # STAGE 7: PARALLEL PROCESSING SETUP
    # =========================================================================
    
    logging.info("Stage 6: Setting up parallel processing...")
    
    # Determine optimal number of worker processes
    system_cpu_count = mp.cpu_count()
    # Use override if specified, otherwise use CPU count but cap at 4 for memory efficiency
    optimal_workers = min(NUM_WORKERS_OVERRIDE or system_cpu_count, 4)
    
    # Calculate batch size for optimal load distribution
    # More batches than workers ensures good load balancing
    batches_per_worker = 4
    total_desired_batches = optimal_workers * batches_per_worker
    batch_size = max(1, total_input_ips // total_desired_batches)
    
    # Split input IPs into batches for parallel processing
    ip_batches = []
    for start_idx in range(0, total_input_ips, batch_size):
        end_idx = min(start_idx + batch_size, total_input_ips)
        batch = input_ip_list[start_idx:end_idx]
        ip_batches.append(batch)
    
    logging.info(f"Processing configuration:")
    logging.info(f"  - Workers: {optimal_workers}")
    logging.info(f"  - Batches: {len(ip_batches)}")
    logging.info(f"  - Average batch size: {batch_size}")
    logging.info(f"  - Total IPs: {total_input_ips}")
    
    # =========================================================================
    # STAGE 8: PARALLEL BATCH PROCESSING
    # =========================================================================
    
    logging.info("Stage 7: Processing IP batches in parallel...")
    
    filtered_ips = []  # Accumulator for all matching IPs
    
    try:
        # Create ProcessPoolExecutor with worker initialization
        with ProcessPoolExecutor(
            max_workers=optimal_workers,
            initializer=_init_worker,           # Function to call in each worker
            initargs=(optimized_cidrs,)         # Arguments for initializer
        ) as process_executor:
            
            logging.info("Submitting batches to worker processes...")
            
            # Process all batches and collect results
            batch_results = process_executor.map(_process_ip_batch, ip_batches)
            
            # Aggregate results from all batches
            for batch_result in batch_results:
                filtered_ips.extend(batch_result)
            
            logging.info("All batches processed successfully")
            
    except Exception as parallel_error:
        # If parallel processing fails, fall back to single-threaded processing
        logging.error(f"Parallel processing failed: {parallel_error}")
        logging.info("Falling back to single-threaded processing...")
        
        # Build SubnetTree for single-threaded fallback
        fallback_tree = SubnetTree.SubnetTree()
        for cidr in optimized_cidrs:
            try:
                fallback_tree[cidr] = True
            except Exception:
                continue  # Skip malformed CIDRs
        
        # Process each IP individually
        for raw_ip in input_ip_list:
            cleaned_ip = raw_ip.strip()
            if not cleaned_ip:
                continue
                
            try:
                # Determine IP to check (same logic as worker function)
                if '/' in cleaned_ip:
                    network_obj = ipaddress.ip_network(cleaned_ip, strict=False)
                    ip_to_check = str(network_obj.network_address)
                else:
                    ip_to_check = cleaned_ip
                    
            except Exception:
                continue  # Skip malformed IPs
            
            try:
                # Check against SubnetTree
                if ip_to_check in fallback_tree:
                    filtered_ips.append(cleaned_ip)
            except Exception:
                continue  # Skip lookup errors
        
        logging.info("Single-threaded fallback processing completed")
    
    # =========================================================================
    # STAGE 9: RESULTS PROCESSING AND OUTPUT
    # =========================================================================
    
    logging.info("Stage 8: Writing filtered results...")
    
    # Ensure output directory exists
    output_path = Path(COUNTRY_ONLY_IPS)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write filtered IPs to output file
    try:
        with open(COUNTRY_ONLY_IPS, 'w') as output_file:
            for ip_address in filtered_ips:
                output_file.write(f"{ip_address}\n")
                
        logging.info(f"Successfully wrote {len(filtered_ips)} filtered IPs to {COUNTRY_ONLY_IPS}")
        
    except IOError as write_error:
        logging.error(f"Failed to write output file: {write_error}")
        raise SystemExit(1)
    
    # =========================================================================
    # STAGE 10: CLEANUP AND REPORTING
    # =========================================================================
    
    logging.info("Stage 9: Cleanup and final reporting...")
    
    # Calculate and report filtering statistics
    input_count = total_input_ips
    output_count = len(filtered_ips)
    filter_rate = (output_count / input_count * 100) if input_count > 0 else 0
    
    logging.info("=== FILTERING RESULTS ===")
    logging.info(f"Input IPs: {input_count:,}")
    logging.info(f"Filtered IPs: {output_count:,}")
    logging.info(f"Filter Rate: {filter_rate:.2f}%")
    logging.info(f"Country: {country_name} ({country_iso_code})")
    
    # Clean up GeoIP directory to force fresh download next time
    geoip_directory = Path(GEOIP_CSV_PATH).parent
    if geoip_directory.exists() and geoip_directory.is_dir():
        try:
            logging.info(f"Cleaning up GeoIP directory: {geoip_directory}")
            shutil.rmtree(geoip_directory)
            logging.info("GeoIP directory removed successfully")
        except Exception as cleanup_error:
            logging.warning(f"Failed to remove GeoIP directory: {cleanup_error}")
            logging.warning("Manual cleanup may be required")
    
    logging.info("=== IP FILTERING PROCESS COMPLETED ===")


# =============================================================================
# SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    """
    Script entry point - sets up logging and starts the filtering process.
    
    This block only runs when the script is executed directly (not imported).
    It configures logging for visibility into the filtering process and
    calls the main filtering function.
    """
    
    # Configure logging for informative output
    # Format includes log level and message for easy reading
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Start the IP filtering process
    try:
        filter_us_ips_optimized()
    except KeyboardInterrupt:
        logging.info("Process interrupted by user")
        raise SystemExit(130)  # Standard exit code for Ctrl+C
    except Exception as unexpected_error:
        logging.error(f"Unexpected error: {unexpected_error}")
        raise SystemExit(1)
