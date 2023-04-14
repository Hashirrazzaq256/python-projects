# import requests
# from datetime import datetime
# MY_LAT = 31.520370
# MY_LONG = 74.358749
# parameters = {
#     "lat":MY_LAT,
#     "lng":MY_LONG,
#     "formatted":1,
# }
# 
# response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
# response.raise_for_status()
# data = response.json()
#
# sunrise = data["results"]["sunrise"].split("T")[0].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[0].split(":")[0]
# print(sunset)
# print(sunrise)
#
# time_now = datetime.now()

#
#
#
#
#
#
#
# # response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # response.raise_for_status()
# # data = response.json()
from astral.sun import sun
from astral import LocationInfo
from datetime import datetime, time

city = LocationInfo("Lahore", "Pakistan")

s = sun(city.observer, date=datetime.now())
sunrise = s['sunrise'].time()
sunset = s['sunset'].time()

print(sunrise)
print(sunset)
