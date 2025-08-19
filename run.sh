#!/bin/bash
set -e

# Where to save raw files
INPUT_DIR="/data/input"
TMP_INPUT="/tmp/all_input.txt"

mkdir -p "$INPUT_DIR"
> "$TMP_INPUT"

# Split args: URLs vs flags
URLS=()
FLAGS=()
for arg in "$@"; do
  if [[ "$arg" == http* ]]; then
    URLS+=("$arg")
  else
    FLAGS+=("$arg")
  fi
done

echo "[INFO] Downloading ${#URLS[@]} files..."
for url in "${URLS[@]}"; do
  fname="$(basename "$url")"
  echo "[INFO] → $url → $INPUT_DIR/$fname"
  wget -q -O "$INPUT_DIR/$fname" "$url"
done

# Concatenate everything
cat "$INPUT_DIR"/*.txt > "$TMP_INPUT"

echo "[INFO] Aggregating..."
python /app/__main__.py -s "${FLAGS[@]}" < "$TMP_INPUT" > /data/output/aggregated.txt

# Clean up downloaded input files
echo "[INFO] Cleaning up input directory..."
# rm -rf /data/input/

# NEW STEP: Filter to US-only IPs
echo "[INFO] Filtering US-only IPs..."
python /app/filter_us_ips.py
