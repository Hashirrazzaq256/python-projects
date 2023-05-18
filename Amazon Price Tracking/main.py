import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
URL = "https://www.amazon.com/VIZIO-Chromecast-Mirroring-Streaming-Channels/dp/B092Q1TRJC/ref=sr_1_1?crid=EK701TXCW6K2&keywords=TV&qid=1684394723&s=electronics&sprefix=tv%2Celectronics-intl-ship%2C395&sr=1-1&th=1"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
           "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.89",
           "Accept-Encoding":"gzip, deflate, br",
           }
response = requests.get(url=URL,headers=headers)
HTML = response.text
soup = BeautifulSoup(HTML,"lxml")
tag = soup.find(name="span",class_ ="a-offscreen")
price = tag.getText()
price = price.split("$")[1]
price = float(price)
print(price)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 160

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("YOUR_EMAIL", "YOUR_PASSWORD")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="YOUR_EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )