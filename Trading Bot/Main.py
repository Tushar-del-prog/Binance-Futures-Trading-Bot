import argparse

from binance_client import BinanceClient
from logger import logger

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)

args = parser.parse_args()
if args.side.upper() not in ["BUY", "SELL"]:
    print("Side must be BUY or SELL")
    exit()

if args.type.upper() not in ["MARKET", "LIMIT"]:
    print("Type must be MARKET or LIMIT")
    exit()

if args.quantity <= 0:
    print("Quantity must be greater than 0")
    exit()

client = BinanceClient()

try:

    if args.type.upper() == "MARKET":

        response = client.place_market_order(
            args.symbol.upper(),
            args.side.upper(),
            args.quantity
        )

    elif args.type.upper() == "LIMIT":

        if args.price is None:
            print("Price is required for LIMIT order.")
            exit()

        response = client.place_limit_order(
            args.symbol.upper(),
            args.side.upper(),
            args.quantity,
            args.price
        )

    else:
        print("Invalid order type")
        exit()

    print("\n===== ORDER SUCCESS =====")

    print("Order ID :", response["orderId"])
    print("Status :", response["status"])
    print("Executed Qty :", response["executedQty"])

    logger.info(f"Market order placed successfully. ID: {response['orderId']}")

    if "avgPrice" in response:
        print("Average Price :", response["avgPrice"])

except Exception as e:

    print("\nOrder Failed")
    print(e)