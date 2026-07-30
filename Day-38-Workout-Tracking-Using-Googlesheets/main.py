import requests
from datetime import datetime
import os

# --- Personal Bio Constants ---
GENDER = "male"
WEIGHT_KG = 54
HEIGHT_CM = 168
AGE = 20

# --- Environment Variables & API Secrets ---
# Retrieve API identifiers and secrets from environment variables for security
APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

# Prompt user for plain-text description of workouts (e.g. "ran 3 miles and walked 20 mins")
exercise_text = input("Tell me which exercises you did: ")

# --- Nutritionix API Call ---
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Post natural language exercise query to Nutritionix to calculate calories and duration
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# --- Date & Time Formatting ---
# Retrieve current date (DD/MM/YYYY) and time (HH:MM:SS) strings
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Bearer Token authorization header for Sheety integration
bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

# --- Sheety Google Sheets Logging Loop ---
# Loop through all exercises recognized by the API and append each row to Google Sheets
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Dispatch HTTP POST request to append new row in Google Sheet via Sheety
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)