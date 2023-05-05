import requests
from pprint import pprint
SHEETY_ENDPOINT = "https://api.sheety.co/b91141a675f3cb9b04118ce4ef6dab41/flightDeals/prices"
class DataManager:


    def __init__(self):
        self.destination_data= {}
    def get_information(self):
        sheety_endpoint = SHEETY_ENDPOINT
        sheety_response = requests.get(url=sheety_endpoint)
        data = sheety_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

     #This class is responsible for talking to the Google Sheet.
