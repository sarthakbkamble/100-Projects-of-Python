
import requests
class DataManager:
    def __init__(self,username,projectName,sheetName,password):
        self.sheety_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"
        self.headers = {
            "Authorization" : f"Basic {password}"
        }
        self.destination_data = {}
        

    def get_data(self):
        response = requests.get(self.sheety_endpoint,headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data