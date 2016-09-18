import Abacus.Models.budgetItem as budgetItem
import decimal

class Expense(budgetItem.BudgetItem):
    """
    Holds the Data Regarding an Expense item in a budget
    """

    def __init__(self, name, ammount = None,
                 percIncome = None, maximum = None):

        self.name = name
        # FIXME: This is stupid!
        self.ammount = None
        self.percIncome = None
        if maximum is not None:
            self.maximum = decimal.Decimal(maximum)
        else:
            self.maximum = maximum
        # Convert Floats to Decimal Values
        if ammount != None:
            ammount = decimal.Decimal(ammount)
            # Calculate the percentage of income by ammount spend
            self.ammount = ammount
            
        elif percIncome != None:
            percIncome = decimal.Decimal(percIncome)
            # Calculate Ammount by Percentage of income
            self.percIncome = percIncome

        else:
            raise ValueError("Ammount or precent of Income must be specified")
        