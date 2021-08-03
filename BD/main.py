import smtplib
import datetime as dtime
import pandas as pd
import random
from email.message import EmailMessage
import time

df = pd.read_csv("birthdays.csv")
# current day and month
current_day = dtime.datetime.now().day
current_month = dtime.datetime.now().month

current_day = 13
current_month = 11
# save the rows that has the current day in new variable
new_df = df.loc[df['day'] == current_day]
# check the length of new_df of the current month
if len(new_df.loc[new_df['month'] == current_month]) > 0:
    # check the length of people having birthday in this day
    for i in range(len(new_df.loc[new_df['month'] == current_month])):
        with open(f"./bd_letters/letter_{random.randint(1, 3)}.txt") as letter_file:
            letter_contents = letter_file.read()
            the_letter = letter_contents.replace("[NAME]", new_df["name"][i])
            # here start using smtplib package to send the letter
            # new connection
            with smtplib.SMTP("smtp.gmail.com") as con:
                # secure the mail
                con.starttls()
                # login
                con.login(user="Ahmedbashatest1@gmail.com", password="")
                # create the msg

                msg = EmailMessage()
                msg["From"] = "Ahmedbashatest1@gmail.com"
                msg["To"] = new_df["email"][i]
                msg["Subject"] = "Happy Birthday !!!🎊"
                msg.set_content(the_letter)

                # send the email
                con.send_message(msg)
                # time delay
                time.sleep(10)
