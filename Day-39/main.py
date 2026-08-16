#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests_cache
import data_manager
import os 
from dotenv import load_dotenv
from datetime import datetime,timedelta
from flight_search import FlightSearch

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

load_dotenv()

# ==================== Talk to Sheety ====================
SHEETY_USERNAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]

mydatamanager = data_manager.DataManager(username=SHEETY_USERNAME,projectName="flightDeals",sheetName="prices",password=SHEETY_PASSWORD)
sheet_data = mydatamanager.get_data()

# ==================== Set the Dates ====================
today = datetime.today().date()
tomorrow = datetime.today().date() + timedelta(days=1)
six_month_from_today = datetime.today().date() + timedelta(days=60)

# ==================== Do a Flight Search ====================
flight_search = FlightSearch()
flights = flight_search.check_flights(
    origin_city_code="LHR",
    destination_city_code="CDG",
    from_time=tomorrow,
    to_time=six_month_from_today
)

print(flights)

