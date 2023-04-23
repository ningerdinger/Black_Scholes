import numpy as np
from scipy.stats import norm
import logging
logger = logging.getLogger(__name__)

class BS():
    def __init__(self, S: float, K: float, T: int, r:float, sigma: float, *args: float):
        """_summary_

        Args:
            S (float): _description_
            K (float): _description_
            T (int): _description_
            r (float): _description_
            sigma (float): _description_

        Returns:
            _type_: _description_
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
        """"""
        return self.d1, self.d2
    
    def calculate_d(self):
        self.d1 = (np.log(self.S/self.K) + (self.r + self.sigma**2/2)*self.T) / (self.sigma*np.sqrt(self.T))
        self.d2 = self.d1 - self.sigma*np.sqrt(self.T)
        return self.d1, self.d2
    
    def BS_CALL(self):
        call = self.S * self.N(self.d1) - self.K * np.exp(-self.r*self.T)* self.N(self.d2)
        return call

    def BS_PUT(self):
        put = self.K*np.exp(-self.r*self.T)*self.N(-self.d2) - self.S*self.N(-self.d1)
        return put
