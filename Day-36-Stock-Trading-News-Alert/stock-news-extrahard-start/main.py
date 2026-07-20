import requests,requests_cache
import os
from dotenv import load_dotenv
from datetime import datetime,timedelta

load_dotenv()

today = datetime.now().date()
yesterday = today - timedelta(days=2)
day_before_yesterday = today - timedelta(days=3)
print(yesterday)
print(day_before_yesterday)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_price_endpoint = "https://www.alphavantage.co/query"
stock_price_api_key = os.environ.get("APLHAVANTAGE_STOCKS_PRICE_API_KEY")

stock_price_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey": stock_price_api_key,
}

stock_price_response = requests.get(url=stock_price_endpoint,params=stock_price_params)
stock_price_response.raise_for_status()

stock_price_data = stock_price_response.json()

# yesterday_price_data = float(stock_price_data["Time Series (Daily)"][str(yesterday)]["4. close"])
# day_before_yesterday_price_data = float(stock_price_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])
# price_difference = ((yesterday_price_data-day_before_yesterday_price_data)/day_before_yesterday_price_data)*100
# if abs(price_difference)>=5:
#     print("Get News")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 


news_endpoint = "https://newsapi.org/v2/everything"
news_api_key = os.environ.get("NEWS_API_KEY")
news_params = {
    "q":"Tesla AND (stock OR market OR Elon Musk)",
    "pagesize" : 3,
    "language":"en",
    "sortBy" : "popularity",
    "apikey":news_api_key,
    "from":day_before_yesterday,
    "to":yesterday,
}

news_response = requests.get(url=news_endpoint,params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
news_articles = news_data["articles"]
articles = []
for article in news_articles:
    article_dict = {
        "title":article["title"],
        "author":article["author"],
        "description":article["description"],
    }
    articles.append(article_dict)

print(articles)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

