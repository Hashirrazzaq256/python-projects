import time
import requests
from astral.sun import sun
from astral import LocationInfo
from datetime import datetime
import smtplib
MY_LAT = 31.520370
MY_LONG = 74.358749
My_EMAIL = "xapastron@gmail.com"
MY_PASSWORD = "yudlqggkbjtyhcjo"

def iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 :
       return True
    


#----------------------------MY Location Sunrise/Sunset Time Check------------------------------------------
def is_dark_outside():

    city = LocationInfo("Lahore", "Pakistan")

    s = sun(city.observer, date=datetime.now())
    sunrise = s['sunrise'].time().hour
    sunset = s['sunset'].time().hour
    if datetime.now().hour< sunrise or datetime.now().hour > sunset:
        return True
while True:
    time.sleep(60)
    if iss_location() and is_dark_outside():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=My_EMAIL,password=MY_PASSWORD)
            connection.sendmail(
                from_addr=My_EMAIL,
                to_addrs=My_EMAIL,
                msg="Subject:Look Up\n\n The ISS is Above you in the sky "
            )
