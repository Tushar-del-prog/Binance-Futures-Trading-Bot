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

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/binance-futures-bot.git
cd binance-futures-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Keys

Open `config.py` and add your Binance Testnet API Key & Secret:

```python
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
BASE_URL = "https://testnet.binancefuture.com"
```

---

## ▶️ How to Run

### Place a MARKET Order

```bash
python bot.py market
```

### Place a LIMIT Order

```bash
python bot.py limit
```

---

## 📊 Logs

All trade activity is stored inside the `logs/` folder:

- `market_order.log` → MARKET order execution details
- `limit_order.log` → LIMIT order execution details

---

## ⚠️ Assumptions

- Binance Futures Testnet account is used
- API keys are valid and activated
- Sufficient testnet balance available
- Internet connection is stable

---

## 📌 Sample Output

```
===== ORDER SUCCESS =====
Order ID : 123456789
Status : FILLED
Executed Qty : 0.001
```

---

## 👨‍💻 Author

Developed as part of a learning project for Binance Futures API integration using Python.
