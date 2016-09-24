from abc import ABC
import decimal
decimal.getcontext().prec = 5

class BudgetItem(ABC):
    """
    abstract Class to for any budget item
    
    """
    
    ### MAGIC METHODS ###
    def __str__(self):
        if self.Ammount is None:
            outputString = "%s: %1.2f percent of income" %(self.Name, self.PercIncome * 100);
        else:
            outputString ="%s: $%1.2f" %(self.Name, self.Ammount);
        return outputString;

    def __init__(self, name, ammount, percIncome):
        self.Name = name;
        self.Ammount = ammount;
        self.PercIncome = percIncome;

    ### GETTERS AND SETTERS ###
    # I don't know if we realy need the getters/setters for Name
    @property
    def Name(self):
        return self._name;
    
    @Name.setter
    def Name(self, name):
        self._name = name;
    
    @property
    def Ammount(self):
        return self._ammount;
    
    @Ammount.setter
    def Ammount(self, ammount):
        if ammount is not None:
            self._ammount = decimal.Decimal(ammount);
        else:
            self._ammount = ammount;
    
    @property
    def PercIncome(self):
        return self._percIncome;
    
    @PercIncome.setter
    def PercIncome(self, PercIncome):
        if PercIncome is not None:
            self._percIncome = decimal.Decimal(PercIncome);
        else:
            self._percIncome = PercIncome;
    

    ### CLASS METHODS ###
    # TODO: RENAME THIS METHOD:
    def calculate_ammount_from_percent(self, Income: float)->None:
        self.Ammount = Income * self.PercIncome;

    def calculate_percent_from_ammount(self, Income: float)->None:
        self.PercIncome = self.Ammount / Income
    
    def drop(self):
        del self;
