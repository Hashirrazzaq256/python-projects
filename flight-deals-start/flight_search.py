import requests
from flight_data import FlightData
API_ENDPOINT_TEQUILA = " https://api.tequila.kiwi.com"
API_KEY_TEQUILA = "CzM0C8TpUF_ByJZi9zN5N7f_or0LP3VV"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self,city_name):
        location_endpoint= f"{API_ENDPOINT_TEQUILA}/locations/query"
        headers ={"apikey":API_KEY_TEQUILA}
        query={"term":city_name,"location_types":"city"}
        response = requests.get(url=location_endpoint,params=query,headers=headers)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": API_KEY_TEQUILA}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=f"{API_ENDPOINT_TEQUILA}/v2/search",
            headers=headers,
            params=query,
        )
        data = response.json()["data"][0]
        # pprint(data)

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data