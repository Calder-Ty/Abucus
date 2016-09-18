class Expense(object):
    """
    Holds the Data Regarding an Expense item in a budget
    """

    def __init__(self, name, ammount = None,
                 percIncome = None, maximum = None):

        self.name = name
        self.ammount = None
        self.percIncome = None
        if maximum is not None:
            self.maximum = deci.Decimal(maximum)
        else:
            self.maximum = maximum
        # Convert Floats to Decimal Values
        if ammount != None:
            ammount = deci.Decimal(ammount)
            # Calculate the percentage of income by ammount spend
            self.ammount = ammount
            
        elif percIncome != None:
            percIncome = deci.Decimal(percIncome)
            # Calculate Ammount by Percentage of income
            self.percIncome = percIncome

        else:
            raise ValueError("Ammount or precent of Income must be specified")
        