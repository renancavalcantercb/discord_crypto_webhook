from dotenv import load_dotenv
import os
from crypto_data import Crypto
from crypto_chart import CryptoChart
from discord_webhook import send_embed

load_dotenv()

CRYPTOCOIN = "bomber-coin"
CURRENCY = "brl"
WEBHOOK_URL = os.getenv("WEBHOOK_URL")


def main():
    crypto_data = Crypto(CRYPTOCOIN, CURRENCY).get_market_chart()
    crypto_chart = CryptoChart(crypto_data, CRYPTOCOIN, CURRENCY)
    crypto_chart._save_chart_as_image("bcoin_chart.png")
    send_embed(WEBHOOK_URL, crypto_data)


if __name__ == "__main__":
    main()
