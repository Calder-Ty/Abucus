"""
Module for the Budget Model
"""
import logging
# Generate Logging file
logging.basicConfig(filename='../abucus.log',level = logging.DEBUG)


class Paycheck(object):
    """
    Object for Holding Data Regarding a Paycheck
    """

    def __init__(self, Type, tax, hours = None,
                 wage = None, salary = None):
        
        if Type == 'Hourly':
            self.gross = hours * wage
        elif Type == 'Salary':
            self.gross = salary
        else:
            raise ValueError("Type must be Salary or Hourly")

        self.tax = self.gross * tax
        self.net = self.gross - self.tax



        
                
