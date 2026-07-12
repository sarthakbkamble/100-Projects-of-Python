import requests
from twilio.rest import Client
import os

from dotenv import load_dotenv

load_dotenv()

# MY_Lat = 16.731967
# MY_Lon = 74.240184
MY_Lat = 75.559693
MY_Lon = 12.7576938
MY_LOCATION = (MY_Lat,MY_Lon)
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

response = requests.get(url=api_endpoint,params=parameters)
response.raise_for_status()
data = response.json()
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
            to="whatsapp:+919156891611"
            )
        print(message.status)