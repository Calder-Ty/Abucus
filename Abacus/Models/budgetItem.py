from abc import ABC
import decimal
decimal.getcontext().prec = 5

class BudgetItem(ABC):
    """
    abstract Class to for any budget item
    
    """
    
    ### MAGIC METHODS ###
    def __str__(self):
        if Ammount is None:
            outputString = "%s: %f percent of income" %(self.Name, self.PercIncome * 100);
        else:
            outputString ="%s: $%1.2f" %(self.Name, self.Ammount)

    def __init__(self, name, ammount, percIncome):
        self.Name = name;
        self.Ammount = ammount;
        self.PercIncome = percIncome;

    ### GETTERS AND SETTERS ###
    # I don't know if we realy need the getters/setters for Name
    @property
    def Name(self):
        return _name;
    
    @Name.setter
    def Name(self, Name):
        self._name = Name;
    
    @property
    def Ammount(self):
        return _ammount;
    
    @Ammount.setter
    def Ammount(self, Ammount):
        if Ammount is not None:
            self.Ammount = decimal.Decimal(Ammount);
        else:
            self.Ammount = Ammount
    
    @property
    def PercIncome(self):
        return _percIncome;
    
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
        self.__del__();
