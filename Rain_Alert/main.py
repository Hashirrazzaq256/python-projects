import requests
api_key = "541f022c20f1ac5300c2f663c99d1445"
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather?lat=31.561920&lon=74.348083&appid=541f022c20f1ac5300c2f663c99d1445")
data = response.json()
print(data)
