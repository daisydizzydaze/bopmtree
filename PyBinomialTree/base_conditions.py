# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 00:27:34 2022

@author: leeca
"""

from datetime import datetime
from dateutil import parser

class base_asset:
    
    """
    Instance variables:
        
    - ``S0`` - float
    - ``div`` - float
    - ``div_yield``  - float
    - ``ex_div_date`` - str or None
    - ``ex_div_step`` - int or None

    Public methods:
        
    - ``dividend_info()`` print summary of dividend information

    """
    
    def __init__(self, S0, div = 0, div_yield = 0, ex_div_date = None, ex_div_step = None):
        """
            
        :param S0: underlying asset spot price at t = 0
        :type S0: float
        :param div: known dollar dividend. Default 0
        :type div: float
        :param div_yield: known dividend yield. Default 0
        :type div_yield: float
        :param ex_div_date: Ex-dividend date. Default None
        :type ex_div_date: str
        :param ex_div_step: Number of steps from t = 0 in which Ex-dividend occurs. Default None
        :type ex_div_date: int


        """

        
        if ex_div_date is not None and ex_div_step is not None:
            raise ValueError('ex_div_date and ex_div_step cannot both be set!')
            
        if div != 0.0 and div_yield != 0.0:
            raise ValueError('div and div_yield cannot both be set!')
        
        if ex_div_step != None:
            assert type(ex_div_step) == int, 'ex_div_step needs to be an integer!'
        
        self.spot_price = S0
        self.dividend_dollar = div
        self.dividend_yield = div_yield
        self.ex_div_date = parser.parse(ex_div_date) if ex_div_date!= None else None
        self.ex_div_step = ex_div_step
        
    def dividend_info(self):
        """
        Method to provide info on dividend payment.

        Returns
        -------
        None.

        """
        
        info1 = 'Dollar dividends: \t ${0:.2f}.\n'.format(self.dividend_dollar)
        info2 = 'Dividend yield: \t {0:.2f}%.\n'.format(self.dividend_yield)
        
        info4 = 'Dividend to occur at step {}.'.format(self.ex_div_step)
        
        if self.ex_div_date == None:
            if self.ex_div_step == None:
                print("No dividend payment expected during the course of the contract.")
            else:
                
                if self.dividend_dollar !=0:
                    print(info1+info4)
                elif self.dividend_yield != 0:
                    print(info2+info4)
                else:
                    print("No dividend payment expected during the course of the contract.")
                    
        else:
            info3 = 'Ex-Dividend date: \t {:%Y-%m-%d}.'.format(self.ex_div_date)
            if self.dividend_dollar !=0:
                print(info1+info3)
            elif self.dividend_yield != 0:
                print(info2+info3)
            else:
                print("No dividend payment expected during the course of the contract.")
                
class base_rate:
    """
    Instance variables:
        
    - ``r`` - float

    """
    
    def __init__(self, r):
        """
            
        :param r: domestic interest rate
        :type r: float


        """
        
        self.rate = r

# =============================================================================
# class base_specs:
#     """
#     Instance variables:
#         
#     - ``T`` - int
#     - ``N`` - int
# 
#     """
#     
#     def __init__(self, T, N):
#         """
#             
#         :param T: time to expiry
#         :type T: int
#         :param N: Number of steps from t = 0 to expiry
#         :type N: int
# 
#         """        
#         
#         assert (T > 0) & (type(T) == int), 'T needs to be an integer with value greater than 0!'
#         assert (N > 0) & (type(N) == int), 'N needs to be an integer with value greater than 0!'
#         self.time_to_expiry = T
#         self.step = N
#         self.delta_t = T/N
# =============================================================================
        