import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "Ahmedbashatest@gmail.com"
MY_PASSWORD = password
MY_LAT = 21.245277
MY_LNG = 40.412512


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    # if response.status_code == 404:
    #     raise Exception("does not exist")

    response.raise_for_status()

    data = response.json()
    iss_lng = float(data["iss_position"]["longitude"])
    iss_lat = float(data["iss_position"]["latitude"])
    # if the ISS is near from my location lat = 21 => 21-5 = 16,lat = 21 => 21+5 = 26
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5:
        return True

    # iss_position = (lng, lat)


# for the sunrise and sunset

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

    response.raise_for_status()

    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_time = datetime.now()
    # print(current_time.hour)
    # to check if it dark or not
    if current_time.hour >= sunset or current_time.hour <= sunrise:
        # it's dark
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        con = smtplib.SMTP("smtp.gmail.com")
        con.starttls()
        con.login(MY_EMAIL, MY_PASSWORD)
        con.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=user_email,
            msg="Subject:Look Up\n\nThe international space station is above you in the sky"
        )
