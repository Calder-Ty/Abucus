"""
Module for the Budget Model
"""
import logging
from decimal import Decimal
# Generate Logging file
logging.basicConfig(filename='../abucus.log',level = logging.DEBUG)


class Paycheck(object):
    """
    Object for Holding Data Regarding a Paycheck
    """

    def __init__(self, Type, tax, name, hours = None,
                 wage = None, salary = None):

        self.name = name
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

    def __init__(self, name, parent, ammount = None,
                 percIncome = None, maximum = None):

        self.name = name
        self.parent = parent
        
        if ammount != None:
            
            # Calculate the percentage of income by ammount spend
            self.ammount = ammount
            self.percIncome = ammount / parent.gross
            
        elif percIncome != None:
            
            # Calculate Ammount by Percentage of income
            self.percIncome = percIncome
            self.ammount = parent.gross * self.percIncome

        else:
            raise ValueError("Ammount or precent of Income must be specified")
        
        self.maximum = maximum



class SavingsItem(object):
    """
    Holds the data regarding a savings item in a budget
    """

    def __init__(self, name, parent, ammount = None, percIncome = None):

        self.name = name
        self.parent = parent
        
        if ammount != None:
            
            # Calculate the percentage of income by ammount spend
            self.ammount = ammount
            self.percIncome = ammount / parent.gross
            
        elif percIncome != None:
            
            # Calculate Ammount by Percentage of income
            self.percIncome = percIncome
            self.amount = parent.gross * self.percIncome

        else:
            raise ValueError("Ammount or precent of Income must be specified")



class Budget(object):
    """
    The budget class puts together paychecks, Expenses and savings to
    create syestem of record
    """

    def __init__(self):
        self.paychecks = {}
        self.expenses = {}
        self.savings = {}
        self.gross = 0
        self.net = 0
        self.disposable = 0

    def addPaycheck(self, *args, **kwargs):

        paycheck = Paycheck(*args, **kwargs)
        self.paychecks[paycheck.name] = paycheck
        self.update()

    def addExpense(self, *args, **kwargs):
        
        if len(self.paychecks) >= 0:
            expense = ExpenseItem(*args, **kwargs)
            self.expenses[expense.name] = expense
            self.update()
        else:
            logger.debug("Attempt to add expense when no income specified")

    def addSavings(self, *args, **kwargs):
        
        if len(self.paychecks) >= 0:
            saving = SavingsItem(*args, **kwargs)
            self.savings[saving.name] = saving
            self.update()
        else:
            logger.debug("Attempt to add savings when no income specified")

            
    def update(self):
        # TODO: Update calculations 
        pass
    

        

    

        
                
