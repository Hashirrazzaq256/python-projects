from datetime import datetime
import os
import requests
import json
APP_ID = os.environ["APP_ID"]
API_KEY = "5ef3d068cb0eb54d64fd0695746cef9d"
excercise_query = input("What exercise did you do today?")
Track_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/b91141a675f3cb9b04118ce4ef6dab41/workout/workouts"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
    "x-remote-user-id": "0"
}
data = {
    "query": excercise_query,
    "gender": "female",
    "weight_kg": 68.04,
    "height_cm": 175.26,
    "age": 35,

}
header ={
"Authorization": "Bearer hahahahehehe"
}

response = requests.post(url=Track_endpoint, headers=headers, json=data)
print(response.json())
data = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    workout = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheet_response = requests.post(sheety_endpoint, json=workout,headers=header)

print(sheet_response.text)
