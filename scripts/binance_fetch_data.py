import requests
import json
import os
from datetime import datetime

def fetch_binance_data(symbol):
    url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    symbols = ["BTCUSDT", "ETHUSDT"]
    all_data = {}

    for symbol in symbols:
        data = fetch_binance_data(symbol)
        all_data[symbol] = data

    date_str = datetime.now().strftime("%Y-%m-%d")
    os.makedirs('../data/binance', exist_ok=True)
    for symbol, data in all_data.items():
        with open(f"data/binance/{symbol}_{date_str}.json", "w") as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()

