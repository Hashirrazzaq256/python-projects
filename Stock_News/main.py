import requests


STOCK_API_KEY = "O4HF1DD900H0PMJS"
NEWS_API_KEY = "246593cc25c441aaac39afa82bb0ad20"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters= {
    "function":"TIME_SERIES_DAILY_ADJUSTED",
     "symbol":STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
params = {
    "q" : COMPANY_NAME,
    "searchin": "description",
}

response = requests.get(url=STOCK_ENDPOINT,params=parameters)
data = response.json()

data["Time Series (Daily)"]
# print(data)
#--------Yesterday DATA----------------
data_list = [value for (key,value) in data.items()]
stock_data = data_list[1]
# print(data_list[1])
tesla_data = [value for (key,value) in stock_data.items()]
yesterday_data = tesla_data[0]
yesterday_data_close = yesterday_data["4. close"]
print(yesterday_data_close)

# print(len(data_list))

#DAY BEFORE YESTERDAY DATA--------

day_before_yesterday = tesla_data[2]
day_before_yesterday_close = day_before_yesterday["4. close"]
print(day_before_yesterday_close)

#--------Positive difference between stock prices --------
difference = abs(float(yesterday_data_close) - float(day_before_yesterday_close))
print(difference)

# --------Percentage difference between two stocks-----------
diff_percent = difference/ float(yesterday_data_close)*100
# if diff_percent >=5 :
news_response = requests.get(NEWS_ENDPOINT,params=params)
news_response.raise_for_status()
