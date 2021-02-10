from datetime import datetime
import requests

print("Stock price with Alpha Vantage")
print()
choice = "y"
while choice.lower() == "y":
    symbol = input("Enter stock symbol:     ")
    print()
    symbol_f = str(symbol)
    main_api = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols='
    api_key = '&apikey=0KT7H1J8FI94FE50'
    url = main_api + symbol_f + api_key
    json_data = requests.get(url).json()
    open_price = float(json_data["Stock Quotes"][0]["2. price"])
    share_value = open_price
    print (share_value)


    choice = input("Continue (y/n)?: ")
    print()
print('Bye')








