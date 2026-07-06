from binance.client import Client
from config import API_KEY, API_SECRET

class BinanceClient:

    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):

        order = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        return order


    def place_limit_order(self, symbol, side, quantity, price):

        order = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        return order