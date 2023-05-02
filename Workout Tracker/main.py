
import requests
import json
APP_ID = "37bc4db1"
API_KEY = "5ef3d068cb0eb54d64fd0695746cef9d"

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "x-remote-user-id": "0"
}
data = {
    "query": "I ran 3 miles and walked 2 miles",
    "gender": "female",
    "weight_kg": 68.04,
    "height_cm": 175.26,
    "age": 35,
    
}
response = requests.post(url, headers=headers, json=data)
print(response.json())
