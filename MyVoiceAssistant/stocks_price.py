import requests
stocks = [
    { 'name': 'Apple Inc.', 'symbol': 'AAPL' },
    { 'name': 'Microsoft Corporation', 'symbol': 'MSFT' },
    { 'name': 'Amazon.com, Inc.', 'symbol': 'AMZN' },
    { 'name': 'Facebook, Inc.', 'symbol': 'FB' },
    { 'name': 'Alphabet Inc.', 'symbol': 'GOOGL' },
    { 'name': 'Tesla, Inc.', 'symbol': 'TSLA' },
    { 'name': 'Netflix, Inc.', 'symbol': 'NFLX' },
    { 'name': 'NVIDIA Corporation', 'symbol': 'NVDA' },
    { 'name': 'Johnson & Johnson', 'symbol': 'JNJ' },
    { 'name': 'Procter & Gamble Co.', 'symbol': 'PG' },
    { 'name': 'Coca-Cola Co.', 'symbol': 'KO' },
    { 'name': "McDonald's Corporation", 'symbol': 'MCD' },
    { 'name': 'Visa Inc.', 'symbol': 'V' },
    { 'name': 'Mastercard Incorporated', 'symbol': 'MA' },
    { 'name': 'Berkshire Hathaway Inc.', 'symbol': 'BRK-A' }
]

# Access the data for the first stock in the array
# print("Company Name: " + stocks[0]['name'])
# print("Ticker Symbol: " + stocks[0]['symbol'])

# Loop through all the stocks in the array and print their data
# for stock in stocks:
#     print("Company Name: " + stock['name'])
#     print("Ticker Symbol: " + stock['symbol'])
#     print("\n")







def get_stock_price(symbol):
    api_key = 'COMRFM2UK1YORB53'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    
    # make a GET request to the Alpha Vantage API
    response = requests.get(url)
    
    # parse the JSON response
    data = response.json()
    
    # check if the API returned an error
    if 'Error Message' in data:
        return "Sorry, I couldn't retrieve the stock data. Please try again later."
    
    # extract the stock price from the JSON response
    price = data['Global Quote']['05. price']
    
    return f"The current price of {symbol} is {price} USD."

if __name__ == '__main__':
   
        symbol = input("Enter the stock symbol: ")
        result = get_stock_price(symbol)
        
        print(result)