import Abacus.Models.paycheck as paycheck

class SalaryCheck(paycheck.Paycheck):
    """
    Class that makes a Paycheck that pays a salary
    
    This class inherits many of it's methods from paycheck, 
    it exists only to keep interface for salary and wages seperate
    to keep it clean. It has no special Properites of its own
    However it does actualy assign real values to many of its inherited
    properties. I should realy make paycheck.Paycheck an abstract class.
    """
    
    ### MAGIC METHODS ###
    def __init__(self, taxRate: float, name: str, salary: float):
        super().__init__(taxRate,name);
        self.Type = "Salary";
        self.Gross = salary;
        self.Tax = self.Gross * self.TaxRate;
        self.Net = self.Gross - self.Tax;

