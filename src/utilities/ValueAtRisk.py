import numpy as np
from scipy.stats import norm
import pandas as pd
import logging
import math

logger = logging.getLogger(__name__)

class VaR():
    def __init__(self, df: pd.DataFrame, names: list, portfolio: list, sensitivity: float=1.0, horizon: int=1, *args: list):
        """
        Args:
            df (pd.DataFrame): provide a dataframe with the data
            names (list): list of the column names that needs to be processed
            portfolio (list): value of each portfolio
            *args (list): if sensitivity or horizon are also provided, they can be given in a list. 
            A checker has not been built in properly. If they aren't given then they take 1 by default. 
            I assumed it was 1 by default due to the excel formula
        """
        self.df = df
        self.names = names
        self.portfolio = portfolio
        self.sensitivity = sensitivity
        self.horizon = horizon

        if args:
            try: # a checker for args still needs to be build in for args
                self.sensitivity = args[0] 
                self.horizon = args[1]
            except Exception:
                logging.info("An error has occured while parsing the args parameter")

    def ln_data(self):
        """
        natural logarithm of the market data
        """
        try:
            for self.name in self.names:
                self.df[self.name] = self.df[self.name].astype(float)
                self.df["ln_"+self.name] = np.log(self.df[self.name])
        except Exception:
            logging.info("An error has occured while making the ln column")
        return self.df
        
    def day_shift(self):
        """
        Calculate the scenario PnL on the basis of t and t-1 which are expressed as x and y respectively.
        """
        for name in self.names:
            list_shift = []
            for i in range(len(self.df)-1):
                x = self.df[name].iloc[i]
                y = self.df[name].iloc[i+1]
                list_shift.append(
                    self.sensitivity*(
                    math.exp(
                    math.log(x)-math.log(y)*self.horizon
                    )-1
                    )
                    )
            list_shift.append("NaN")
            self.df["day_shift_"+name[-5:]] = list_shift
        return self.df
    
    def pnl_vectors(self):
        """
        Calculate the pnl data on basis of the dayshift from the method above.
        """
        df = self.day_shift()
        self.shift_names = ["day_shift_"+name[-5:] for name in self.names]
        list_pnl = []
        for j in range(len(self.shift_names)):
            list_pnl = []
            for i in range(len(df)-1):
                value = df[self.shift_names[j]].iloc[i]
                list_pnl.append(value*self.portfolio[j])
            list_pnl.append(None)
            df["pnl_vector_"+self.names[j][-5:]] = list_pnl
        return df
    
    def total_pnl(self):
        """
        Calculate the total pnl on basis of all pnl vectors that were calculated
        """
        df = self.pnl_vectors()
        self.pnl_names = ["pnl_vector_"+name[-5:] for name in self.names]
        df['total_pnl'] = df[self.pnl_names].sum(axis=1)
        return df

    def one_day_var(self):
        """
        Calculate the one day var on basis of the total pnl. Formula is 0.4*z2+0.6z3 
        where z2, z3 stands for the second smallest and third smallest total pnl value respectively
        """
        df = self.total_pnl()
        second_smallest = df["total_pnl"].nsmallest(2).iloc[-1]
        third_smallest = df["total_pnl"].nsmallest(3).iloc[-1]
        oneD_var = 0.4*second_smallest + 0.6*third_smallest
        return oneD_var
