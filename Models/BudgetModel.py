"""
Module for the Budget Model, contains the classes: Paycheck, ExpenseItem,
SavingsItem, and budget
"""
import logging
import decimal as deci
# Generate Logging file
logging.basicConfig(filename='../abucus.log',level = logging.DEBUG)



class Paycheck(object):
    """
    Object for Holding Data Regarding a Paycheck
    """

    def __init__(self, Type, tax, name, hours = None,
                 wage = None, numWeeks = 4, salary = None):


        # Convert the float values to Decimal Values
        tax = deci.Decimal(tax)
        numWeeks = deci.Decimal(numWeeks)
        self.name = name
        if Type == 'Hourly':
            hours = deci.Decimal(hours)
            wage = deci.Decimal(wage)
            self.gross = hours * wage * numWeeks
        elif Type == 'Salary':
            salary = deci.Decimal(salary)
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
        
        # Convert Floats to Decimal Values
        if ammount != None:
            ammount = deci.Decimal(ammount)
            # Calculate the percentage of income by ammount spend
            self.ammount = ammount
            self.percIncome = deci.Decimal(ammount) / parent.gross
            
        elif percIncome != None:
            percIncome = deci.Decimal(percIncome)
            # Calculate Ammount by Percentage of income
            self.percIncome = percIncome
            self.ammount = parent.gross * self.percIncome

        else:
            raise ValueError("Ammount or precent of Income must be specified")
        
        self.maximum =deci.Decimal(maximum)



class SavingsItem(object):
    """
    Holds the data regarding a savings item in a budget
    """

    def __init__(self, name, parent, ammount = None, percIncome = None):

        self.name = name
        self.parent = parent
        
        if ammount != None:
            
            # Calculate the percentage of income by ammount spend
            self.ammount = deci.Decimal(ammount)
            self.percIncome = self.ammount / parent.gross
            
        elif percIncome != None:
            
            # Calculate Ammount by Percentage of income
            self.percIncome = deci.Decimal(percIncome)
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

    def addPaycheck(self, Type, tax, name, hours = None,
                 wage = None, numWeeks = 4, salary = None):

        paycheck = Paycheck(Type, tax, name, hours = hours,
                 wage = wage, numWeeks = numWeeks, salary = salary)
        self.paychecks[paycheck.name] = paycheck
        self.update()

    def addExpense(self,  name, parent, ammount = None,
                 percIncome = None, maximum = None):
        
        if len(self.paychecks) >= 0:
            expense = ExpenseItem( name, parent, ammount = ammount,
                 percIncome = percIncome, maximum = maximum)
            self.expenses[expense.name] = expense
            self.update()
        else:
            logger.debug("Attempt to add expense when no income specified")

    def addSavings(self, name, parent, ammount = None, percIncome = None):
        
        if len(self.paychecks) >= 0:
            saving = SavingsItem(name, parent, ammount = ammount, percIncome = percIncome)
            self.savings[saving.name] = saving
            self.update()
        else:
            logger.debug("Attempt to add savings when no income specified")

            
    def update(self):
        # TODO: Update calculations Possibly push part of these out to the seperate methods
        self.gross = 0
        self.net = 0
        for i in self.paychecks:
            self.gross += self.paychecks[i].gross
            self.net += self.paychecks[i].net

        self.disposable = self.net
        for i in self.expenses:
            self.disposable -= self.expenses[i].ammount

        for i in self.savings:
            self.disposable -= self.savings[i].ammount

        self.net = round(self.net, ndigits = 2)
        self.gross = round(self.gross, ndigits = 2)
        self.disposable = round(self.disposable, ndigits = 2)


    def remove(self, Obj):
        name = Obj.name
        if type(Obj) is BudgetModel.Paycheck:
            del self.paychecks[name]
        
        elif type(Obj) is BudgetModel.ExpenseItem:
            del self.expenses[name]
        
        elif type(Obj) is BudgetModel.SavingsItem:
            del self.savings[name]

        else:
            logger.debug("%s type is undefined for the Remove method", name)
        
