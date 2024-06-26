
# Crypto Data Scraper

## Описание

`Crypto Data Scraper` - это проект, предназначенный для получения данных о криптовалютах с различных криптобирж и сохранения этих данных в файлы. Проект реализован на Python и Bash, и позволяет пользователю выбирать биржу и криптовалюту для получения данных, а также выводит обработанные данные в виде удобочитаемой таблицы.

## Структура проекта

```
crypto-data-scraper/
├── data/
│   ├── binance/
│   ├── coinbase/
│   └── kraken/
├── scripts/
│   ├── binance_fetch_data.py
│   ├── coinbase_fetch_data.py
│   ├── kraken_fetch_data.py
│   ├── fetch_data.sh
│   ├── process_data.py
│   └── process_data.sh
├── main.sh
├── README.md
└── requirements.txt
```

- **data/**: Директория для хранения данных, полученных с различных бирж.
  - **binance/**: Данные с Binance.
  - **coinbase/**: Данные с Coinbase.
  - **kraken/**: Данные с Kraken.
- **scripts/**: Директория со скриптами.
  - **binance_fetch_data.py**: Python скрипт для получения данных с Binance.
  - **coinbase_fetch_data.py**: Python скрипт для получения данных с Coinbase.
  - **kraken_fetch_data.py**: Python скрипт для получения данных с Kraken.
  - **fetch_data.sh**: Bash скрипт для запуска соответствующего Python скрипта на выбор пользователя.
  - **process_data.py**: Python скрипт для обработки и форматирования данных.
  - **process_data.sh**: Bash скрипт для запуска скрипта обработки данных.
- **main.sh**: Главный Bash файл для запуска программы.
- **README.md**: Этот файл.
- **requirements.txt**: Файл с зависимостями проекта.

## Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/crypto-data-scraper.git
cd crypto-data-scraper
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

## Использование

### 1. Запуск программы

Запустите главный Bash скрипт и следуйте инструкциям на экране:

```bash
bash main.sh
```

### 2. Получение данных

При запуске `main.sh`, вам будет предложено выбрать биржу для получения данных:

```text
Выберите биржу для получения данных:
1. Binance
2. Coinbase
3. Kraken
```

Введите номер соответствующей биржи и данные будут загружены и сохранены в соответствующую директорию.

### 3. Обработка данных

После получения данных, вы можете обработать их и вывести в виде удобочитаемой таблицы:

```bash
bash main.sh
```

Выберите пункт меню для обработки данных:

```text
Выберите действие:
1. Получить данные
2. Обработать данные
```

После выбора пункта "Обработать данные", скрипт выведет данные, разделенные по биржам, в виде таблицы.

## Пример данных

После выполнения скриптов, данные будут сохранены в формате JSON в соответствующих директориях внутри `data/`. Например:

```
data/
├── binance/
│   ├── BTCUSDT_2024-05-19.json
│   └── ETHUSDT_2024-05-19.json
├── coinbase/
│   ├── BTC-USD_2024-05-19.json
│   └── ETH-USD_2024-05-19.json
├── kraken/
│   ├── XXBTZUSD_2024-05-19.json
│   └── XETHZUSD_2024-05-19.json
...
```

### Пример вывода таблицы

```
Binance - данные
+----------+-------------+-----------------+-------------+------------+
| Symbol   | Last Price  | Price Change (%)| High Price  | Low Price  |
+----------+-------------+-----------------+-------------+------------+
| BTCUSDT  | 35000.00    | 1.5             | 36000.00    | 34000.00   |
| ETHUSDT  | 2500.00     | 2.0             | 2600.00     | 2400.00    |
+----------+-------------+-----------------+-------------+------------+

Coinbase - данные
+---------+-------------+-----------------+-------------+------------+
| Symbol  | Last Price  | Price Change (%)| High Price  | Low Price  |
+---------+-------------+-----------------+-------------+------------+
| BTC-USD | 35000.00    | N/A             | N/A         | N/A        |
| ETH-USD | 2500.00     | N/A             | N/A         | N/A        |
+---------+-------------+-----------------+-------------+------------+

Kraken - данные
+----------+-------------+-----------------+-------------+------------+
| Symbol   | Last Price  | Price Change (%)| High Price  | Low Price  |
+----------+-------------+-----------------+-------------+------------+
| XXBTZUSD | 35000.00    | 1.5             | 36000.00    | 34000.00   |
| XETHZUSD | 2500.00     | 2.0             | 2600.00     | 2400.00    |
+----------+-------------+-----------------+-------------+------------+
```

## Автоматизация с помощью cron

Вы можете настроить cron для автоматического запуска скриптов. Например, чтобы запускать скрипт каждую минуту, добавьте следующую строку в ваш crontab:

```bash
* * * * * /bin/bash /path/to/crypto-data-scraper/main.sh
```

## Вклад

Вы можете свободно вносить свой вклад в проект. Для этого форкните репозиторий, создайте новую ветку для ваших изменений и создайте pull request.

```bash
git checkout -b feature-branch
# Внесите изменения и закоммитьте их
git push origin feature-branch
```

## Лицензия

Этот проект лицензируется под лицензией apache. См. файл LICENSE для получения дополнительной информации.

---
