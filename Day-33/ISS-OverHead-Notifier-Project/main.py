import requests
from datetime import datetime
import smtplib
import time

# --- Configuration Constants ---
# Set up default email credentials and geographical coordinates (defaults to London)
MY_EMAIL = "sarthakwrkonly@gmail.com"
MY_PASSWORD = ""
MY_LAT = 51.507351 
MY_LONG = -0.127758 


def is_iss_overhead():
    """Fetches the current live position of the ISS via API and checks if it is within range."""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status() # Raise an exception if the API request fails
    data = response.json()

    # Parse and convert coordinates to floats
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Determine if the user's position is within a +5 or -5 degree margin of the ISS position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    """Queries astronomical sunrise and sunset times to check if it is currently dark outside."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, # Request unformatted ISO-8601 UTC datetimes
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    
    # Parse UTC ISO-8601 timestamps and extract the hour value (e.g., "2026-07-16T21:45:00+00:00")
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current hour from the local machine's system time
    time_now = datetime.now().hour

    # It is considered night if the current hour is after sunset or before sunrise
    if time_now >= sunset or time_now <= sunrise:
        return True


# --- Background Monitoring Loop ---
# Continually monitor the sky condition and ISS tracking coordinates every 60 seconds
while True:
    time.sleep(60)
    
    # Send an email alert only if the station is close enough and it is dark enough to see it
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls() # Secure the network payload using TLS encryption
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )