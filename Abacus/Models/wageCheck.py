import Abacus.Models.paycheck as paycheck

class WageCheck(paycheck.Paycheck):
    """
    Class that makes a Paycheck that pays a wage

    """

    def __init__(self, taxRate: float, name: str, hours: float,
                 wage: str, numWeeks: int = 4):
                 
        self.Hours = hours;
        self.Wage = wage;
        self.NumWeeks = numWeeks;
        super().__init__(taxRate, name);
        self.Type = "Hourly";
        self.Gross = self.Hours * self.Wage * self.NumWeeks;
        self.Tax = self.Gross * self.TaxRate;
        self.Net = self.Gross - self.Tax;
        
