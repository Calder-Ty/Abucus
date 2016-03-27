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



class ExpenseItem(object):
    """
    Holds the Data Regarding an Expense item in a budget
    """

    def __init__(self, name, parent, ammount = None, percIncome = None,
                 maximum = None):

        self.name = name
        self.parent = parent
        if ammount != None:
            pass
        elif percIncome != None:
            pass
        else:
            raise ValueError("Ammount or precent of Income must be specified")
        
        self.maximum = maximum


class SavingsItem(object):
    """
    Holds the data regarding a savings item in a budget
    """

    def __ini__(self, name, parent, ammount = None, percIncome = None):

        self.name = name
        self.parent = parent
        if ammount != None:
            pass
        elif percIncome != None:
            pass
        else:
            raise ValueError("Ammount or Percent of Income must be specified")
    

        
                
