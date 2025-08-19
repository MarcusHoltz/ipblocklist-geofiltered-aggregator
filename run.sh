#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Safely load environment variables from .env while ignoring comments and empty lines
while IFS='=' read -r key value; do
  # Ignore lines that are comments or empty
  if [[ ! "$key" =~ ^# && -n "$key" ]]; then
    export "$key=$value"
  fi
done < .env

# Where to save raw files
INPUT_DIR="/data/input"
TMP_INPUT="/tmp/all_input.txt"
OUTPUT_DIR="/data/output"

# Create the input and output directories if they don't exist
mkdir -p "$INPUT_DIR"
mkdir -p "$OUTPUT_DIR"
> "$TMP_INPUT"

# Load LIST variables dynamically into an array
LISTS=()
for var in $(env | grep '^LIST_' | cut -d= -f1); do
  LISTS+=("${!var}")  # Append value of each LIST_ variable to the LISTS array
done

# Ensure the LISTS array is populated
if [ ${#LISTS[@]} -eq 0 ]; then
  echo "[ERROR] No LIST URLs found in the environment variables!"
  exit 1
fi

# Correct URLs, with the fixed URL for emerging threats
echo "[INFO] Downloading ${#LISTS[@]} files..."
for url in "${LISTS[@]}"; do
  fname="$(basename "$url")"  # Extract the file name from the URL
  echo "[INFO] → $url → $INPUT_DIR/$fname"
  
  # Download and save file
  wget -q -O "$INPUT_DIR/$fname" "$url"
  
  # Check if wget command succeeds
  if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to download file from $url"
    continue  # Proceed with the next URL if this one fails
  fi
done

# Validate and filter IPs, skip comments or invalid entries (including non-IP data like domain lists and special characters)
echo "[INFO] Validating and filtering IP addresses..."
> "$TMP_INPUT"  # Ensure the temporary file is cleared before adding valid lines
for file in "$INPUT_DIR"/*; do  # Process all files, regardless of extension
  # Get file size and calculate estimated processing time
  file_size=$(stat -c%s "$file" 2>/dev/null || echo "0")
  if [ "$file_size" -gt 0 ]; then
    # Calculate estimated time at 7kb per second
    estimated_seconds=$((file_size / 7000))
    if [ $estimated_seconds -lt 60 ]; then
      time_display="${estimated_seconds}s"
    elif [ $estimated_seconds -lt 3600 ]; then
      minutes=$((estimated_seconds / 60))
      seconds=$((estimated_seconds % 60))
      time_display="${minutes}m ${seconds}s"
    else
      hours=$((estimated_seconds / 3600))
      minutes=$(((estimated_seconds % 3600) / 60))
      time_display="${hours}h ${minutes}m"
    fi
    echo "[INFO] File size: $(numfmt --to=iec-i --suffix=B $file_size), estimated processing time: $time_display"
  fi
  echo "[INFO] Processing file: $file"
  cat "$file" | \
  grep -Ev '^(#.*|^$|[a-zA-Z]+\.[a-zA-Z]+|^/.*|^!.*|^-.*)' | \
  while read -r line; do
    # Relaxed IP validation
    if echo "$line" | grep -Pq '^(?:\d{1,3}\.){3}\d{1,3}(/(?:[1-9]|1[0-2])?\d{1,2})?$'; then
      echo "$line" >> $TMP_INPUT
    else
      echo "[WARNING] Invalid line: $line" >> /data/output/invalid_ips.log
    fi
  done
done

# Check if any IPs were successfully written to TMP_INPUT
if [[ ! -s "$TMP_INPUT" ]]; then
  echo "[ERROR] No valid IP addresses found! Please check the input data."
  exit 1
fi

# Concatenate all valid entries into the temporary file
echo "[INFO] Aggregating..."
# Run the aggregation script with full stdout
# python /app/__main__.py -s "${FLAGS[@]}" < "$TMP_INPUT" > /data/output/aggregated.txt
# Run with cleaner output
python /app/__main__.py -s "${FLAGS[@]}" < "$TMP_INPUT" > /data/output/aggregated.txt 2>/dev/null

# Clean up downloaded input files (optional)
echo "[INFO] Cleaning up input directory..."
 rm -rf /data/input/

# NEW STEP: Filter to COUNTRY_ISO_CODE-only IPs
echo "[INFO] Filtering ${COUNTRY_ISO_CODE}-only IPs..."  # Dynamic log message based on COUNTRY_ISO_CODE
# Run the script to filter out only US-based IPs
python /app/filter_ips.py
