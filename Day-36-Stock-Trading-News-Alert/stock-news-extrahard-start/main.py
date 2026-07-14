import requests,requests_cache
import os
from dotenv import load_dotenv
from datetime import datetime,timedelta
from twilio.rest import Client


# Load environment variables from a .env file
load_dotenv()

# Calculate the target dates for stock price evaluation
today = datetime.now().date()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=4)

# Define constants for the target stock and company
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


# Set up parameters and fetch daily stock data from the Alpha Vantage API
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

# Extract closing prices and calculate the percentage difference between the two dates
yesterday_price_data = float(stock_price_data["Time Series (Daily)"][str(yesterday)]["4. close"])
day_before_yesterday_price_data = float(stock_price_data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])
price_difference = ((yesterday_price_data-day_before_yesterday_price_data)/day_before_yesterday_price_data)*100

# Check if the stock price fluctuation is 5% or more to trigger news retrieval and alerting
if abs(price_difference)>=5:
        
    # Fetch the top 3 relevant English news articles about Tesla from the News API
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
    for news in news_articles:
        article_dict = {
            "title":news["title"],
            "description":news["description"],
        }
        articles.append(article_dict)


    # Format the alert message body with directional indicators based on price movement
    message_to_be_sent = ""
    if price_difference>0:
        message = f"""TSLA: 🔺{abs(int(price_difference))}\n
    Headline: {articles[0]["title"]}\nBrief: {articles[0]["description"]}\n\n
    Headline: {articles[0]["title"]}\nBrief: {articles[1]["description"]}\n\n
    Headline: {articles[0]["title"]}\nBrief: {articles[2]["description"]}\n\n
    """
        message_to_be_sent = message
    else:
        message = f"""TSLA: 🔻{abs(int(price_difference))}\n
    Headline: {articles[0]["title"]}\nBrief: {articles[0]["description"]}\n\n
    Headline: {articles[0]["title"]}\nBrief: {articles[1]["description"]}\n\n
    Headline: {articles[0]["title"]}\nBrief: {articles[2]["description"]}\n\n
    """
        message_to_be_sent = message



    # Initialize the Twilio client and send the formatted alert via WhatsApp
    twilio_acc_sid = os.environ.get("TWILIO_ACCOUNT_SID_FOR_STOCK_PRICES_ALERT")
    twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN_FOR_STOCK_PRICES_ALERT")
    my_number = os.environ.get("MY_PHONE_NUMBER")

    client = Client(twilio_acc_sid, twilio_auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f"{message_to_be_sent}",
    to=f"whatsapp:{my_number}"
    )