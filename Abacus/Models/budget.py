"""
Module for the Budget Model, contains the classes: Paycheck, ExpenseItem,
SavingsItem, and budget
"""

import logging
import Abacus.Models.expense as expense
import Abacus.Models.paycheck as paycheck
import Abacus.Models.savings as savings

# Generate Logging file
logging.basicConfig(filename='../abucus.log',level = logging.DEBUG)


class Budget(object):
    """
    The budget class puts together paychecks, Expenses and savings to create syestem of record.

    Properties
    paychecks (Dict): Dictionary containing all paychecks associated with the budget
    expenses (Dict): Dictionary containing all the expenses that are associated with Budget
    savings (Dict): Dictionary containing all the savings that are associated with the Budget
    gross (Decimal): Value that is the Sum of all Income from the paychecks
    net (Decimal): Value that is the sum of all the Income From the Paychecks minus taxes
    disposable (Decimal): Value that is equal to all of the net income not assigned to an expense or savings
    """

    def __init__(self):
        self.paychecks = {};
        self.expenses = {};
        self.savings = {};
        self.gross = 0;
        self.net = 0;
        self.disposable = 0;

    def addPaycheck(self, paycheck: paycheck.Paycheck) -> None:
        """
        Adds paycheck to the paycheck property

        @params
        paycheck: an object of Type Model.Paycheck
        """
        self.paychecks[paycheck.name] = paycheck;
        self.update();

    def addExpense(self, expense: expense.Expense)-> None:
        """
        Adds expense to expense property

        @params
        expense: and object of type Model.Expense
        """
        if len(self.paychecks) >= 0:

            if expense.percIncome is None:
                expense.percIncome = expense.ammount / self.gross;
            else:
                expense.ammount = self.gross * expense.percIncome;
            self.expenses[expense.name] = expense;
            self.update();
        else:
            logger.debug("Attempt to add expense when no income specified");
            raise Exception("Attempt to add Expense when no income specified");
                

    def addSavings(self, savings: savings.Savings)-> None:
        """
        Adds a Savings object to the savings property

        @param
        savings: and object of type Model.Savings
        """
        if len(self.paychecks) >= 0:

            if saving.percIncome is None:
                saving.percIncome = saving.ammount / self.gross;
            else:
                saving.ammount = self.gross * saving.percIncome;
            self.savings[saving.name] = saving;
            self.update();
        else:
            logger.debug("Attempt to add savings when no income specified")
            raise Exception("Attempt to add Expense when no income specified");

            
    def update(self)-> None:
        """
        updates The budgets records to keep track of Gross, Net, and other values
        """
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


#    def remove(self, Obj)-> None:
#
#        # TODO: Move deletion duties to the individual classes
#        name = Obj.name
#        if type(Obj) is BudgetModel.Paycheck:
#            del self.paychecks[name]
#        
#        elif type(Obj) is BudgetModel.ExpenseItem:
#            del self.expenses[name]
#        
#        elif type(Obj) is BudgetModel.SavingsItem:
#            del self.savings[name]

#        else:
#            logger.debug("%s type is undefined for the Remove method", name)
#            except TypeError:
#                print("%s type is undefined for the Remove method", name)        
