import numpy as np
from scipy.stats import norm
import logging
logger = logging.getLogger(__name__)

class BS():
    def __init__(self, S: float, K: float, T: float, r:float, sigma: float, *args: float):
        """
        The black scholes model with spot price
        Args:
            S (float): Spotprice
            K (float): Strike price
            T (int): Time to expiry
            r (float): interest rate
            sigma (float): volatility
        """
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        if args:
            self.d1 = args[0]
            self.d2 = args[1]
        else:
            try: 
                self.d1, self.d2 = self.calculate_d()
            except Exception:
                logging.info("A mistake has been made")
                
        self.N = norm.cdf

    def get_d(self):
        """
        Returns d1 and d2
        """
        return self.d1, self.d2
    
    def calculate_d(self):
        """
        Calculates d1 and d2 if they are not provided
        """
        self.d1 = (np.log(self.S/self.K) + (self.r + self.sigma**2/2)*self.T) / (self.sigma*np.sqrt(self.T))
        self.d2 = self.d1 - self.sigma*np.sqrt(self.T)
        return self.d1, self.d2
    
    def BS_CALL(self):
        """
        The black scholes call option
        """
        call = self.S * self.N(self.d1) - self.K * np.exp(-self.r*self.T)* self.N(self.d2)
        return call

    def BS_PUT(self):
        """
        The black scholes put option
        """
        put = self.K*np.exp(-self.r*self.T)*self.N(-self.d2) - self.S*self.N(-self.d1)
        return put
