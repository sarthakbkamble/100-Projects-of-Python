import requests
from twilio.rest import Client
import os

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up geographic coordinates, API credentials, and query parameters for the weather forecast
# MY_Lat = 16.731967
# MY_Lon = 74.240184
MY_Lat = 75.559693
MY_Lon = 12.7576938
MY_LOCATION = (MY_Lat,MY_Lon)
my_number = os.environ.get("MY_PHONE_NUMBER")
api_key = os.environ.get("WEATHER_API_KEY")
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast" 
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
parameters ={
    "lat":MY_Lat,
    "lon":MY_Lon,
    "appid":api_key,
    "cnt":4,    
}

# Fetch the upcoming weather forecast data from the OpenWeatherMap API
response = requests.get(url=api_endpoint,params=parameters)
response.raise_for_status()
data = response.json()

# Parse the forecast slots and trigger a WhatsApp rain alert via Twilio if any weather ID indicates precipitation
for dict in data["list"]:
    weather = {
        "weather id":dict["weather"][0]["id"],
        "description" : dict["weather"][0]["description"],
    }
    if weather["weather id"] < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body="It's going to rain today. Remember to bring an umbrella ☔",
            to=f"whatsapp:{my_number}"
            )
        print(message.status)