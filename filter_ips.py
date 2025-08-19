import os
import pandas as pd
import requests
import logging
import ipaddress
from pathlib import Path

# Paths
GEOIP_CSV_PATH = '/data/geoip/geoip2-ipv4.csv'
OUTPUT_PATH = '/data/output/aggregated-us-only.txt'
INPUT_PATH = '/data/output/aggregated.txt'

# Download the GeoIP CSV file if not present
def download_geoip_file():
    if not os.path.exists(GEOIP_CSV_PATH):
        logging.info(f"{GEOIP_CSV_PATH} not found. Downloading...")
        url = "https://datahub.io/core/geoip2-ipv4/r/geoip2-ipv4.csv"
        response = requests.get(url)
        if response.status_code == 200:
            with open(GEOIP_CSV_PATH, 'wb') as f:
                f.write(response.content)
            logging.info("GeoIP2 CSV file downloaded successfully.")
        else:
            logging.error(f"Failed to download GeoIP2 CSV file. HTTP status code: {response.status_code}")
            exit(1)

# Filter IPs to only US-based ones
def filter_us_ips():
    # Download GeoIP file if necessary
    download_geoip_file()

    # Load the CSV with the GeoIP information
    df = pd.read_csv(GEOIP_CSV_PATH)

    # Check if required columns are available
    if 'country_iso_code' not in df.columns and 'country_name' not in df.columns:
        logging.error("GeoIP2 CSV file must contain 'country_iso_code' or 'country_name'.")
        exit(1)

    # Filter based on country (US)
    us_networks = df[ 
        (df.get('country_iso_code') == 'US') | 
        (df.get('country_name') == 'United States')
    ]['network'].dropna().tolist()

    # Log number of US networks found
    logging.info(f"Found {len(us_networks)} US networks in the GeoIP data.")

    # Convert the networks to ipaddress objects for easy comparison
    us_networks = [ipaddress.ip_network(cidr) for cidr in us_networks]

    # Load the aggregated IPs
    with open(INPUT_PATH, 'r') as f:
        ip_list = f.readlines()

    # Filter IPs by US networks
    us_ips = []
    for ip in ip_list:
        ip = ip.strip()
        try:
            ip_obj = ipaddress.ip_network(ip)
        except ValueError:
            logging.warning(f"Skipping invalid IP/network: {ip}")
            continue

        # Check if the IP falls within any US network
        for us_net in us_networks:
            if ip_obj.subnet_of(us_net) or ip_obj == us_net:
                us_ips.append(ip)
                break

    # Write the filtered US-only IPs to the output file
    with open(OUTPUT_PATH, 'w') as f:
        for ip in us_ips:
            f.write(f"{ip}\n")

    logging.info(f"Filtered {len(us_ips)} US-based IPs into {OUTPUT_PATH}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    filter_us_ips()
