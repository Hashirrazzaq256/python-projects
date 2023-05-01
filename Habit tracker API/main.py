import requests
from datetime import datetime as dt
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hahahahehehe"
USERNAME = "hashir21"
user_params = {
    "token": TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai",

}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json= graph_config, headers= headers)
# print(response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = dt.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes you have coded today?"),
}
response = requests.post(url=pixel_creation_endpoint,json= pixel_data,headers= headers)
print(response.text)
