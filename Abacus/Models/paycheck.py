import budgetItem

class Paycheck(budgetItem.BudgetItem):
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
