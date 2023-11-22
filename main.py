import smtplib
import datetime as dt
import random

MY_EMAIL = "drajner22@gmail.com"
MY_PASSWORD = "clvbvcersotzxkbv"


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 2:
    with open("quotes.txt", mode="r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )