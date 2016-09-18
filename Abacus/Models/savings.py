import Abacus.Models.budgetItem as budgetItem
import decimal

class Savings(budgetItem.BudgetItem):
    """
    Holds the data regarding a savings item in a budget
    """

    def __init__(self, name, ammount = None, percIncome = None):

        self.name = name
        # FIXME: This is Stupid!
        self.percIncome = None
        self.ammount = None
        
        if ammount != None:
            
            # Calculate the percentage of income by ammount spend
            self.ammount = decimal.Decimal(ammount)
            
        elif percIncome != None:
            
            # Calculate Ammount by Percentage of income
            self.percIncome = decimal.Decimal(percIncome)

        else:   
            raise ValueError("Ammount or precent of Income must be specified")
