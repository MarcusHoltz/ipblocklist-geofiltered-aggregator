# Install dependencies

FROM python:3.12-slim

RUN apt-get update && apt-get install -y bash curl wget
#RUN pip install requests
RUN pip install pandas requests ipaddress

WORKDIR /app

COPY __main__.py /app/
COPY run.sh /app/
COPY filter_us_ips.py /app/

# Install Python deps
#RUN pip install pandas

# Download GeoIP2 CSV
RUN wget -O geoip2-ipv4.csv https://datahub.io/core/geoip2-ipv4/r/geoip2-ipv4.csv

ENTRYPOINT [ "bash", "/app/run.sh" ]
