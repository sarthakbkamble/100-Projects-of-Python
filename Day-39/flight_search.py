from dotenv import load_dotenv
import os , requests

load_dotenv()

SERPAPI_ENDPOINT = "https://serpapi.com/search"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["SERPAPI_API_KEY"]
        

    def check_flights(self,origin_city_code, destination_city_code, from_time, to_time):
        serpapi_parameters = {
            "engine" : "google_flights",
            "departure_id": origin_city_code,
            "arrival_id":destination_city_code,
            "outbound_date":from_time.strftime("%Y-%m-%d"),
            "return_date":to_time.strftime("%Y-%m-%d"),
            "type":"1",
            "adults":"1",
            "currency":"GBP",
            "api_key": self._api_key,
        }
        response = requests.get(SERPAPI_ENDPOINT,params=serpapi_parameters)

        if response.status_code !=200:
            print(f"check_flights() response code: {response.status_code}")
            return None
        
        flight_data = response.json()
        if "error" in flight_data:
            print(f"API error: {flight_data["error"]}")
            return None
        return flight_data
