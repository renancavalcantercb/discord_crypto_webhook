from pycoingecko import CoinGeckoAPI
from utils.log_manager import LogManager
import datetime

cg = CoinGeckoAPI()
logger = LogManager.get_logger(__name__)


class Crypto:
    def __init__(self, crypto_name, currency, days=1):
        """
        Initializes the Crypto class.

        Args:
            crypto_name (str): The name of the cryptocurrency.
            currency (str): The currency to compare the cryptocurrency to.
            days (str, optional): The number of days to get the market chart for. Defaults to 1.
        """
        self.crypto_name = crypto_name
        self.currency = currency
        self.days = days

    def get_price(self):
        return cg.get_price(ids=self.crypto_name, vs_currencies=self.currency)

    def get_market_chart(self):
        logger.info(f"Getting market chart for {self.crypto_name}")
        chart_data = cg.get_coin_market_chart_by_id(
            id=self.crypto_name, vs_currency=self.currency, days=self.days
        )
        logger.info(f"Got market chart for {self.crypto_name}")
        return self._transform_data(chart_data)

    def get_coin_info(self):
        return cg.get_coin_by_id(id=self.crypto_name)

    def _transform_data(self, data):
        timestamps = []
        values = []
        for timestamp, value in data.get("prices"):
            timestamp = datetime.datetime.fromtimestamp(timestamp / 1000)
            timestamps.append(timestamp)
            values.append(value)

        return {"timestamps": timestamps, "values": values}
