#This file is still under construction

import logging
logger = logging.getLogger(__name__)

class validate:
    def __init__(self, config: dict):
        """Validates whether the config provided is feasible. If it is not then it will return the appropiate error and log it.
        This function has to be called from the main

        Args:
            config (dict): The config given.
        """
        self.config = config