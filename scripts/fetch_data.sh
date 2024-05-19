#!/bin/bash

echo "Выберите биржу для получения данных:"
echo "1. Binance"
echo "2. Coinbase"
echo "3. Kraken"

read -p "Введите номер (1/2/3): " exchange

case $exchange in
    1)
        echo "Вы выбрали Binance"
        python3 scripts/binance_fetch_data.py
        ;;
    2)
        echo "Вы выбрали Coinbase"
        python3 scripts/coinbase_fetch_data.py
        ;;
    3)
        echo "Вы выбрали Kraken"
        python3 scripts/kraken_fetch_data.py
        ;;
    *)
        echo "Неправильный выбор"
        exit 1
        ;;
esac

