#!/bin/bash

echo "Выберите действие:"
echo "1. Получить данные"
echo "2. Обработать данные"

read -p "Введите номер (1/2): " action

case $action in
    1)
        bash scripts/fetch_data.sh
        ;;
    2)
        bash scripts/process_data.sh
        ;;
    *)
        echo "Неправильный выбор"
        exit 1
        ;;
esac

