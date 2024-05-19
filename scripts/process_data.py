import json
import os
from tabulate import tabulate

def read_json_files(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename)) as f:
                data.append(json.load(f))
    return data

def process_binance_data(data):
    processed = []
    for item in data:
        processed.append([
            item['symbol'],
            item['lastPrice'],
            item['priceChangePercent'],
            item['highPrice'],
            item['lowPrice']
        ])
    return processed

def process_coinbase_data(data):
    processed = []
    for item in data:
        processed.append([
            item['data']['base'],
            item['data']['amount'],
            "N/A",  # Coinbase API doesn't provide percentage change in this endpoint
            "N/A",
            "N/A"
        ])
    return processed

def process_kraken_data(data):
    processed = []
    for item in data:
        for pair, info in item['result'].items():
            processed.append([
                pair,
                info['c'][0],
                info['p'][0],
                info['h'][0],
                info['l'][0]
            ])
    return processed

def main():
    exchanges = {
        "binance": process_binance_data,
        "coinbase": process_coinbase_data,
        "kraken": process_kraken_data
    }

    for exchange, process_function in exchanges.items():
        directory = f"data/{exchange}"
        data = read_json_files(directory)
        processed_data = process_function(data)

        headers = ["Symbol", "Last Price", "Price Change (%)", "High Price", "Low Price"]
        print(f"{exchange.capitalize()} - данные")
        print(tabulate(processed_data, headers=headers, tablefmt="grid"))
        print("\n")

if __name__ == "__main__":
    main()

