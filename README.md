# Binance-Futures-Trading-Bot
A Python-based trading bot for Binance Futures Testnet supporting MARKET and LIMIT orders with structured logging and error handling.

## 📌 Features

- Place MARKET orders
- Place LIMIT orders
- Structured logging for all trades

- ## 🛠 Tech Stack

- Python 3
- Binance Futures Testnet API
- Requests / python-binance library
- Logging module

---

##  Project Structure

TRADING BOT

Binance client.py
main.py
orders.py
config.py
logger.py
requirements.txt
 
logs
     market_order.log
    limit_order.log

     Add API Keys

Open `config.py` and add your Binance Testnet API Key & Secret:

``python
API_KEY = "UU4H7K3WqoGSx9ozkyGwh23q5LcMdLg2JFhgNab3oqo1oNmpTqPUX7WkR68lMKRx"
API_SECRET = "C7CJfwpWAl7z4A4PL0P6UJhULLQgqNgjjUiHpVHZKne6Of1Pvgts7a7HwTZE87fZ"
BASE_URL = "https://testnet.binancefuture.com"

 How to Run

### Place a MARKET Order

```bash
python bot.py market
```

### Place a LIMIT Order

```bash
python bot.py limit
```

---

##  Logs

All trade activity is stored inside the `logs/` folder:

 `market_order.log` → MARKET order execution details

## Sample Output
 ===== ORDER SUCCESS =====
Order ID : 18949950744
Status : NEW
Executed Qty : 0.0000
