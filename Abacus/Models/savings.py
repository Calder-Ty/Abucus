class SavingsItem(object):
    """
    Holds the data regarding a savings item in a budget
    """

    def __init__(self, name, ammount = None, percIncome = None):

        self.name = name
        self.percIncome = None
        self.ammount = None
        
        if ammount != None:
            
            # Calculate the percentage of income by ammount spend
            self.ammount = deci.Decimal(ammount)
            
        elif percIncome != None:
            
            # Calculate Ammount by Percentage of income
            self.percIncome = deci.Decimal(percIncome)

        else:   
            raise ValueError("Ammount or precent of Income must be specified")
