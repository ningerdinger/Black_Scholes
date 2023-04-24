#This file is still heavy under construction.
from utilities.config_validatior import validate
import logging

logger = logging.getLogger(__name__)

class main():
    def __init__(self, config: dict):
        """_summary_

        Args:
            config (dict): The operating config file which allows you to manage and call all other appropiate functionalities.
        """
        self.config = config
        validate(self.config)
        data_market = config("market_data")
        portfolio_test = config.get("portfolio", None)