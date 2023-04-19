import requests
from twilio.rest import Client
account_sid = 'AC2c66dece96b3eabae7ae7ca89545556e'
auth_token = 'd143366c54184a62799ad598e084ee7f'

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall?lat=31.561920&lon=74.348083&exclude=current,minutely,daily&appid=b2cc51c44c74a937a323c2276f9db551")
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
rain = False
for hour_data in weather_slice:
    condition = hour_data["weather"][0]["id"]
    if int(condition) <700 :
        rain = True
if rain:

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+16205360447',
        body='It is going to rain today.Remember to bring an umbrella',
        to='+923174432613'
    )
    print(message.status)
