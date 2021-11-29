"""
bot to underake algorithmic trading by Harrison Oates
Wont be executing trades as is more of a programming exercise rather than actual bot
Using data at 50 pull req per second from coingecko
"""

# Import numpy for calculation
import numpy as np


# Initialise the api using pycoingecko module found from documentation at
# https://github.com/man-c/pycoingecko
# https://www.coingecko.com/en/api/documentation

from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()
