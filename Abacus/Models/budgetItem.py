from abc import ABC

class BudgetItem(ABC):
    """
    abstract Class to for any budget item
    
    """
    
    def remove(self):
        self.__del__()
