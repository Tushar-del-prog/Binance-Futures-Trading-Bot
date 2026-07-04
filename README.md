# 🚀 Binance Futures Testnet Trading Bot

A simple Python-based trading bot that connects to Binance Futures Testnet and allows users to place MARKET and LIMIT orders with proper logging and error handling.

---

## 📌 Features

- Place MARKET orders
- Place LIMIT orders
- Structured logging for all trades
- Error handling for API requests
- Clean and modular Python code

---

## 🛠 Tech Stack

- Python 3
- Binance Futures Testnet API
- Requests / python-binance library
- Logging module

---

## 📁 Project Structure

```
binance-futures-bot/
│
├── bot.py
├── client.py
├── orders.py
├── config.py
├── logger.py
├── requirements.txt
├── README.md
└── logs/
    ├── market_order.log
    └── limit_order.log
```

---



### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Keys

Open `config.py` and add your Binance Testnet API Key & Secret:

```python
API_KEY = "UU4H7K3WqoGSx9ozkyGwh23q5LcMdLg2JFhgNab3oqo1oNmpTqPUX7WkR68lMKRx"
API_SECRET = "C7CJfwpWAl7z4A4PL0P6UJhULLQgqNgjjUiHpVHZKne6Of1Pvgts7a7HwTZE87fZ"
BASE_URL = "https://testnet.binancefuture.com"
```

---


## 📊 Logs

All trade activity is stored inside the `logs/` folder:

- `market_order.log` → MARKET order execution details

---



## 📌 Sample Output

```
===== ORDER SUCCESS =====
Order ID : 18949950744
Status : NEW
Executed Qty : 0.0000
```

---

## 👨‍💻 Author

Developed as part of a learning project for Binance Futures API integration using Python.
