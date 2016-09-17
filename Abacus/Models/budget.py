"""
Module for the Budget Model, contains the classes: Paycheck, ExpenseItem,
SavingsItem, and budget
"""

import logging
# Generate Logging file
logging.basicConfig(filename='../abucus.log',level = logging.DEBUG)


class Budget(object):
    """
    The budget class puts together paychecks, Expenses and savings to create syestem of record.

    Properties
    paychecks (Dict): Dictionary containing all paychecks associated with the budget
    expenses (Dict): Dictionary containing all the expenses that are associated with 
    Methods
    """

    def __init__(self):
        self.paychecks = {};
        self.expenses = {};
        self.savings = {};
        self.gross = 0;
        self.net = 0;
        self.disposable = 0;

    def addPaycheck(self, Type, tax, name, hours = None,
                 wage = None, numWeeks = 4, salary = None):

        paycheck = Paycheck(Type, tax, name, hours = hours,
                 wage = wage, numWeeks = numWeeks, salary = salary);
        self.paychecks[paycheck.name] = paycheck;
        self.update();

    def addExpense(self,  name, ammount = None,
                 percIncome = None, maximum = None):
        
        if len(self.paychecks) >= 0:
            expense = ExpenseItem( name, ammount = ammount,
                 percIncome = percIncome, maximum = maximum);
            if expense.percIncome is None:
                expense.percIncome = expense.ammount / self.gross;
            else:
                expense.ammount = self.gross * expense.percIncome;
            self.expenses[expense.name] = expense;
            self.update();
        else:
            logger.debug("Attempt to add expense when no income specified");

    def addSavings(self, name, ammount = None, percIncome = None):
        
        if len(self.paychecks) >= 0:
            saving = SavingsItem(name, ammount = ammount, percIncome = percIncome);      
            if saving.percIncome is None:
                saving.percIncome = saving.ammount / self.gross;
            else:
                saving.ammount = self.gross * saving.percIncome;
            self.savings[saving.name] = saving;
            self.update();
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
        
