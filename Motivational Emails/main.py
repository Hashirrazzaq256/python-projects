import smtplib
import datetime as dt
import random
my_email = "kukuraja677@gmail.com"
password = "yonuctydmapgfzxl"

with open("quotes.txt") as data:
    quotes = data.readlines()
def send_quote():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="hashir.razzaq@yahoo.com",msg=f"Subject:hello\n\n{random.choice(quotes)}")

now = dt.datetime.now()
if now.weekday() == 2:
        send_quote()






