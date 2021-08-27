import requests
from twilio.rest import Client

# for twilio
account_sid = "ACCOUNT SID for twilio"
auth_token = 'API for twilio'

client = Client(account_sid, auth_token)

# for weather
endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "API for open weather"

parameters = {
    "lat": 21.2703,
    "lon": 40.4158,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=endpoint, params=parameters)
# print(response.status_code)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data['hourly'][0:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    # print("Take an umbrella")
    message = client.messages \
        .create(
        body="It will rain today. Take an umbrella ☔️",
        from_='My twilio number',
        to='My real number'
    )
    # to see if success or not
    print(message.status)
