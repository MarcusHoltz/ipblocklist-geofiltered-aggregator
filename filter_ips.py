import os
import pandas as pd
import requests
import logging
import ipaddress
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
from dotenv import load_dotenv
import shutil

# Load environment variables from .env file
load_dotenv()

# Fetch country and paths from environment variables
country_iso_code = os.getenv('COUNTRY_ISO_CODE', 'US')  # Default to 'US'
country_name = os.getenv('COUNTRY_NAME', 'United States')  # Default to 'United States'
GEOIP_CSV_PATH = os.getenv('GEOIP_CSV_PATH', '/data/geoip/geoip2-ipv4.csv')
ALL_IPS_FROM_LISTS = os.getenv('ALL_IPS_FROM_LISTS', '/data/output/aggregated.txt')

# Dynamically set the output file path based on country_iso_code
COUNTRY_ONLY_IPS = f'/data/output/aggregated-{country_iso_code.lower()}-only.txt'

# Download the GeoIP CSV file if not present
def download_geoip_file():
    if not os.path.exists(GEOIP_CSV_PATH):
        logging.info(f"{GEOIP_CSV_PATH} not found. Downloading...")
        url = "https://datahub.io/core/geoip2-ipv4/r/geoip2-ipv4.csv"
        response = requests.get(url)
        if response.status_code == 200:
            Path(GEOIP_CSV_PATH).parent.mkdir(parents=True, exist_ok=True)
            with open(GEOIP_CSV_PATH, 'wb') as f:
                f.write(response.content)
            logging.info("GeoIP2 CSV file downloaded successfully.")
        else:
            logging.error(f"Failed to download GeoIP2 CSV file. HTTP status code: {response.status_code}")
            exit(1)

def create_ip_range_list(us_networks):
    """Convert CIDR networks to (start_ip, end_ip) integer ranges for faster lookup"""
    ranges = []
    for network_str in us_networks:
        try:
            network = ipaddress.ip_network(network_str)
            start_ip = int(network.network_address)
            end_ip = int(network.broadcast_address)
            ranges.append((start_ip, end_ip))
        except ValueError:
            continue
    
    # Sort ranges by start IP for potential optimization
    ranges.sort()
    logging.info(f"Created {len(ranges)} IP ranges for lookup")
    return ranges

def is_ip_in_ranges(ip_str, ip_ranges):
    """Check if IP is in any of the US ranges using integer comparison"""
    try:
        # Handle both single IPs and CIDR notation
        if '/' in ip_str:
            network = ipaddress.ip_network(ip_str.strip())
            ip_int = int(network.network_address)
        else:
            ip_int = int(ipaddress.ip_address(ip_str.strip()))
        
        # Binary search would be even faster, but linear is still much better than original
        for start_ip, end_ip in ip_ranges:
            if start_ip <= ip_int <= end_ip:
                return ip_str.strip()
                
    except (ValueError, ipaddress.AddressValueError):
        # Remove verbose logging of invalid IPs
        return None
    
    return None

def process_ip_batch(args):
    """Process a batch of IPs - designed for multiprocessing"""
    ip_batch, ip_ranges = args
    us_ips = []
    
    for ip_str in ip_batch:
        result = is_ip_in_ranges(ip_str, ip_ranges)
        if result:
            us_ips.append(result)
    
    return us_ips

def filter_us_ips_optimized():
    # Download GeoIP file if necessary
    download_geoip_file()

    # Load the CSV with the GeoIP information
    logging.info("Loading GeoIP database...")
    df = pd.read_csv(GEOIP_CSV_PATH)

    # Check if required columns are available
    if 'country_iso_code' not in df.columns and 'country_name' not in df.columns:
        logging.error("GeoIP2 CSV file must contain 'country_iso_code' or 'country_name'.")
        exit(1)

    # Filter based on country (configured dynamically)
    us_mask = (df.get('country_iso_code') == country_iso_code) | (df.get('country_name') == country_name)
    us_networks = df[us_mask]['network'].dropna().tolist()

    logging.info(f"Found {len(us_networks)} {country_name} networks in the GeoIP data.")

    # Create optimized IP ranges for lookup
    ip_ranges = create_ip_range_list(us_networks)

    # Load the aggregated IPs
    logging.info("Loading input IP list...")
    with open(ALL_IPS_FROM_LISTS, 'r') as f:
        ip_list = [line.strip() for line in f if line.strip()]

    # Estimate processing time
    estimated_seconds = len(ip_list) / 450
    if estimated_seconds < 60:
        time_display = f"{estimated_seconds:.0f}s"
    elif estimated_seconds < 3600:
        minutes = int(estimated_seconds / 60)
        seconds = int(estimated_seconds % 60)
        time_display = f"{minutes}m {seconds}s"
    else:
        hours = int(estimated_seconds / 3600)
        minutes = int((estimated_seconds % 3600) / 60)
        time_display = f"{hours}h {minutes}m"
    
    logging.info(f"Estimated processing time: {time_display} at ~450 IPs/second")
    logging.info(f"Processing {len(ip_list)} IPs...")

    # Determine optimal number of processes
    num_processes = min(mp.cpu_count(), 8)  # Cap at 8 to avoid overwhelming the system
    
    # Split IP list into batches for multiprocessing
    batch_size = max(1000, len(ip_list) // (num_processes * 4))  # Ensure reasonable batch size
    ip_batches = [ip_list[i:i + batch_size] for i in range(0, len(ip_list), batch_size)]
    
    logging.info(f"Using {num_processes} processes with {len(ip_batches)} batches of ~{batch_size} IPs each")

    # Process batches in parallel using ProcessPoolExecutor
    us_ips = []
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        # Create arguments for each batch
        batch_args = [(batch, ip_ranges) for batch in ip_batches]
        
        # Process all batches and collect results
        for batch_result in executor.map(process_ip_batch, batch_args):
            us_ips.extend(batch_result)

    # Ensure output directory exists
    Path(COUNTRY_ONLY_IPS).parent.mkdir(parents=True, exist_ok=True)
    
    # Write the filtered Country only IPs to the output file
    with open(COUNTRY_ONLY_IPS, 'w') as f:
        for ip in us_ips:
            f.write(f"{ip}\n")

    logging.info(f"Filtered {len(us_ips)} {country_iso_code.upper()}-based IPs into {COUNTRY_ONLY_IPS}")

    # Remove the GeoIP directory to force re-download on next run
    geoip_dir = Path(GEOIP_CSV_PATH).parent
    if geoip_dir.exists() and geoip_dir.is_dir():
        logging.info(f"Removing GeoIP directory: {geoip_dir}")
        shutil.rmtree(geoip_dir)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    filter_us_ips_optimized()
