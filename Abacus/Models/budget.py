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
    Paychecks (Dict): Dictionary containing all Paychecks associated with the budget
    Expenses (Dict): Dictionary containing all the Expenses that are associated with Budget
    SavingsDict (Dict): Dictionary containing all the savings that are associated with the Budget
    Gross (Decimal): Value that is the Sum of all Income from the Paychecks
    Net (Decimal): Value that is the sum of all the Income From the Paychecks minus taxes
    Disposable (Decimal): Value that is equal to all of the Net income not assigned to an expense or savings
    """

    def __init__(self):
        self.Paychecks = {};
        self.Expenses = {};
        self.SavingsDict = {};
        self.Gross = 0;
        self.Net = 0;
        self.Disposable = 0;

    def addPaycheck(self, pay: paycheck.Paycheck) -> None:
        """
        Adds paycheck to the paycheck property

        @params
        paycheck: an object of Type Model.Paycheck
        """
        self.Paychecks[pay.Name] = pay;
        self.update();

    def addExpense(self, exp: expense.Expense)-> None:
        """
        Adds expense to expense property

        @params
        expense: and object of type Model.Expense
        """
        if len(self.Paychecks) >= 0:
            
            # Set expense properties that need an Income
            if expense.percIncome is None:
                exp.caclulate_percent_from_ammount();
            else:
                exp.calculate_ammount_from_percent();
            
            # We want to make sure that the expense is not
            # Overwriting another one, so make sure it
            # Doesnt already exist in the Expenses list
            if exp.Name not in self.Expenses.keys():
                self.Expenses[expense.Name] = expense;
                self.update();
            else:
                raise Exception("Attempt to put an expense into the budget\
                                with same name as already existing expense");
        else:
            logger.debug("Attempt to add expense when no income specified");
            raise Exception("Attempt to add Expense when no income specified");
                

    def addSavings(self, sav: savings.Savings)-> None:
        """
        Adds a Savings object to the SavingsDict property

        @param
        savings: and object of type Model.Savings
        """
        if len(self.Paychecks) >= 0:

            if saving.percIncome is None:
                sav.calculate_percent_from_ammount();
            else:
                sav.calculate_ammount_from_percent();
            # Want to make sure taht the savings is not
            # overwriting another one, so make sure it
            # Doesn't already exist.    
            if sav.Name not in self.SavingsDict.keys():
                self.SavingsDict[saving.name] = saving;
                self.update();
            else:
                raise Exception("Attempt to put a savings into the budget\
                                 with same name as already existing savings");
        else:
            logger.debug("Attempt to add savings when no income specified");
            raise Exception("Attempt to add Expense when no income specified");

            
    def update(self)-> None:
        """
        updates The budgets records to keep track of Gross, Net, and other values
        """
        # TODO: Update calculations Possibly push part of these out to the seperate methods
        self.Gross = 0
        self.Net = 0
        for i in self.Paychecks:
            self.Gross += self.Paychecks[i].Gross
            self.Net += self.Paychecks[i].Net

        self.Disposable = self.Net
        for i in self.Expenses:
            self.Disposable -= self.Expenses[i].ammount

        for i in self.SavingsDict:
            self.Disposable -= self.SavingsDict[i].ammount

        self.Net = round(self.Net, ndigits = 2)
        self.Gross = round(self.Gross, ndigits = 2)
        self.Disposable = round(self.Disposable, ndigits = 2)


#    def remove(self, Obj)-> None:
#
#        # TODO: Move deletion duties to the individual classes
#        name = Obj.name
#        if type(Obj) is BudgetModel.Paycheck:
#            del self.Paychecks[name]
#        
#        elif type(Obj) is BudgetModel.ExpenseItem:
#            del self.Expenses[name]
#        
#        elif type(Obj) is BudgetModel.SavingsItem:
#            del self.SavingsDict[name]

#        else:
#            logger.debug("%s type is undefined for the Remove method", name)
#            except TypeError:
#                print("%s type is undefined for the Remove method", name)        
