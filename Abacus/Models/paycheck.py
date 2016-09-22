import decimal
decimal.getcontext().prec = 5

class Paycheck(object):
    """
    Object for Holding Data Regarding a Paycheck
    """
    ### CLASS ATTRIBUTES ###
    _ALLOWED_TYPES = ['Salary', 'Hourly']

    ### MAGIC METHODS ###
    def __str__(self):
        print(self.Name + ":\n\t\t" +
                  "Gross: " + self.Gross + "\n\t\t" +
                  "Net: " + self.Net)

    def __init__(self, taxRate: float, name: str):

        # Declare Properties:
        self.Tax = 0;
        self.Net = 0;
        self.Name = name;
        self.Gross = 0;
        self.TaxRate = taxRate;
        self.Type = None;

    ### GETTERS and SETTERS ###
    @property
    def Tax(self):
        return self._tax;
        
    @Tax.setter
    def Tax(self, Tax):
        self._tax = decimal.Decimal(Tax);
    
    @property
    def Net(self):
        return self._net;
    
    @Net.setter
    def Net(self, Net):
        self._net = decimal.Decimal(Net);
    
    @property
    def Name(self):
        return self._name;

    @Name.setter
    def Name(self, Name):
        self._name=Name;
    
    @property
    def Gross(self):
        return self._gross

    @Gross.setter
    def Gross(self, Gross):
        self._gross = decimal.Decimal(Gross)
    
    @property
    def TaxRate(self):
        return self._taxRate

    @TaxRate.setter
    def TaxRate(self, TaxRate):
        self._taxRate = decimal.Decimal(TaxRate)

    @property
    def Type(self):
        return self._type
    
    @Type.setter
    def Type(self, Type):
        if Type in Paycheck._ALLOWED_TYPES or Type is None:
            self._type = Type
        else:
            raise Exception("This Type of Paycheck is not allowed")
        
