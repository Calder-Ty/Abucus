import Abacus.Models.budgetItem as budgetItem
import decimal
decimal.getcontext().prec = 5

class Expense(budgetItem.BudgetItem):
    """
    Holds the Data Regarding an Expense item in a budget

    @Properties:
    Maximum (decimal.Decimal): 
    """
    ### MAGIC METHODS ###
    def __init__(self, name: str, ammount: float = None,
                 percIncome: float = None, maximum: float = None):
        super().__init__(name,ammount,percIncome);
        self.Maximum = maximum;

    ### GETTERS AND SETTERS ###

    @property
    def Maximum(self):
        return _maximum;
    
    @Maximum.setter
    def Maximum(self, Maximum):
        if Maximum is not None:
            self._maximum = decimal.Decimal(Maximum);
        else:
            self._maximum = Maximum;
        