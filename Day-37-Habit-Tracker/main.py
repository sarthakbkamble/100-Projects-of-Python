import requests,os
from datetime import datetime

# --- Configuration & Credentials ---
TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "graph1"

# Get the current system date instance
today = datetime.today()

# --- 1. User Creation Endpoint ---
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# --- 2. Graph Creation Endpoint ---
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name" : "Steps calculator in Kms",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

# response= requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

# Pixela uses a custom HTTP header for API authentication
headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

# --- 3. Post Pixel Data Endpoint (Create) ---
post_endpoint = f"https://pixe.la/v1/users/sarthak112/graphs/graph1"

# Format the current date as 'YYYYMMDD' (e.g. '20260721') as required by Pixela
post_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many kilometers did you cycle today? "),
}

# Post pixel data to the graph
response = requests.post(url=post_endpoint,json=post_config,headers=headers)
print(response.text)

# --- 4. Update Pixel Data Endpoint (Update) ---
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# --- 5. Delete Pixel Data Endpoint (Delete) ---
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"