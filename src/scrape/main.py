import requests
import json
from datetime import datetime
import time
import os

START_YEAR = 2009
DATA_LIMIT = 500
SLEEP_DURATION = 1
OUTPUT_JSON_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'output', 'overview.json')

def fetch_data(start_date, end_date):
    url = f"https://ws.lr.labour.gov.on.ca/arb/*?startDate={start_date}&endDate={end_date}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {start_date} to {end_date}")
        return []

def fetch_data_monthly(year):
    monthly_data = []
    for month in range(1, 13):
        start_date = f"{year}-{month:02d}-01"
        if month == 12:
            end_date = f"{year}-12-31"
        else:
            end_date = f"{year}-{month+1:02d}-01"
        data = fetch_data(start_date, end_date)
        monthly_data.extend(data)
        print(f"Fetched data for {year}-{month:02d}: {len(data)} records")
        time.sleep(SLEEP_DURATION)
    return monthly_data

def integrate_data(start_year, end_year):
    all_data = []
    for year in range(start_year, end_year + 1):
        start_date = f"{year}-01-01"
        end_date = f"{year}-12-31"
        data = fetch_data(start_date, end_date)
        if len(data) >= DATA_LIMIT:
            print(f"Data limit reached for {year}, fetching month by month")
            data = fetch_data_monthly(year)
        all_data.extend(data)
        print(f"Fetched data for {year}: {len(data)} records")
        time.sleep(SLEEP_DURATION)
    return all_data

def save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

end_year = datetime.now().year

all_data = integrate_data(START_YEAR, end_year)
save_to_file(all_data, OUTPUT_JSON_PATH)
