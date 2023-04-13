import pandas
from random import randint
import smtplib
import datetime as dt
# with open("birthdays.csv") as file:


my_email = "xapastron@gmail.com"
password = "aswxvkizpoxrkiot"
data = pandas.read_csv("birthdays.csv")
today = dt.datetime.now()
today_date = (today.month,today.day)


birthday_dicts  = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows() }

if today_date in birthday_dicts:
    birthday_person = birthday_dicts[today_date]
    file = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file) as data_file:
        content = data_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"]
                            ,msg=f"Subject:Birthday Wish \n\n{content}")


else:
    print("no birthday")
