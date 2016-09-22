import Abacus.Models.budgetItem as budgetItem
import decimal
decimal.getcontext().prec = 5

class Savings(budgetItem.BudgetItem):
    """
    Holds the data regarding a savings item in a budget
    """

    def __init__(self, name, ammount = None, percIncome = None):
        super().__init__(name, ammount, percIncome)