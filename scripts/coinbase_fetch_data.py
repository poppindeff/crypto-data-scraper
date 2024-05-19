import requests
import json
import os
from datetime import datetime

def fetch_coinbase_data(symbol):
    url = f"https://api.coinbase.com/v2/prices/{symbol}/spot"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    symbols = ["BTC-USD", "ETH-USD"]
    all_data = {}

    for symbol in symbols:
        data = fetch_coinbase_data(symbol)
        all_data[symbol] = data

    date_str = datetime.now().strftime("%Y-%m-%d")
    os.makedirs('../data/coinbase', exist_ok=True)
    for symbol, data in all_data.items():
        with open(f"data/coinbase/{symbol}_{date_str}.json", "w") as f:
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()

