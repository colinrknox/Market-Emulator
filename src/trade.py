import requests

# Constant strings needed for accessing API
API_KEY = 'Z0LVKBJWV75SJA53'
PRICE_URL_PRE = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
PRICE_URL_POST = f'&outputsize=compact&apikey={API_KEY}'
DATA = 'Meta Data'
LAST = '3. Last Refreshed'
SERIES_1MIN = 'Time Series (1min)'

def get_price(symbol):
    symbol_data = get_json_objects(PRICE_URL_PRE + symbol + PRICE_URL_POST)
    if not symbol_data:
        return None
    last_refreshed = symbol_data[DATA][LAST]
    price_data = symbol_data[SERIES_1MIN]
    return price_data[last_refreshed]

def get_json_objects(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
        json = response.json()
    except (requests.HTTPError, ValueError) as e:
        print(f'Error generating JSON from url:{url}\n{e.message}')
        return None
    else:
        return json
