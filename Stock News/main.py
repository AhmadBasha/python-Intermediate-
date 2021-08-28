import requests
from twilio.rest import Client

# for twilio
account_sid = "twilio account_sid"
auth_token = 'twilio API'

client = Client(account_sid, auth_token)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API = "news api"
STOCK_API = "stock api"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}

news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()

news_data = news_response.json()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

# for yesterday_data
yesterday_data = stock_data_list[0]
yesterday_data_closing_price = yesterday_data['4. close']

# before yesterday data
before_yesterday_data = stock_data_list[1]
before_yesterday_data_closing_price = before_yesterday_data['4. close']



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.

difference = float(yesterday_data_closing_price) - float(before_yesterday_data_closing_price)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# the percentage
diff_percentage = round((difference / float(yesterday_data_closing_price)) * 100)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator
# check if the percentage
if abs(diff_percentage) > 5:
    data_articles = news_data["articles"][0:3]
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    # HINT 1: Consider using a List Comprehension.
    article_data_list = [f"{STOCK}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in data_articles]


for article in article_data_list:
    message = client.messages \
        .create(
        body=article,
        from_='your twilio number',
        to='your phone number'
    )
    # to see if success or not
    print(message.status)

