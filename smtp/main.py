import smtplib
import datetime as dt
import random

# monday == 0
if dt.datetime.now().weekday() == 0:
    with open("quotes.txt")as quotes_file:
        quotes = quotes_file.readlines()
        quote = random.choice(quotes)
    # new connection
    with smtplib.SMTP("smtp.gmail.com") as con:
        # tls = Transport Layer Security ( to secure our connection )
        # so the content of the email will be encrypted
        con.starttls()

        con.login(user="Ahmedbashatest@gmail.com", password="")

        con.sendmail(from_addr="Ahmedbashatest@gmail.com",
                     to_addrs="",
                     msg=f"Subject:Motivation\n\n {quote}")

##########################
# import smtplib
#
# my_email = "Ahmedbashatest@gmail.com"
# pass_ = ""
#
# # con = smtplib.SMTP("smtp.gmail.com")
# # con = smtplib.SMTP("smtp.live.com")
# # con = smtplib.SMTP("smtp.mail.yahoo.com")
#
# with smtplib.SMTP("smtp.gmail.com") as con:
#     # tls = Transport Layer Security ( to secure our connection )
#     # so the content of the email will be encrypted
#     con.starttls()
#
#     con.login(user=my_email, password=pass_)
#
#     con.sendmail(from_addr=my_email,
#                  to_addrs="",
#                  msg="Subject:Hello\n\n This is the body of my email.")

# closing the connection
# con.close()


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year()
# month = now.month()
# day = now.day()
# hour = now.hour()
# minute = now.minute()
# sec = now.second()
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1992, month=11, day=13)
