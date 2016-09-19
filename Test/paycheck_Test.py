from nose.tools import *;
from Abacus.Models.salaryCheck import SalaryCheck
from Abacus.Models.wageCheck import WageCheck
import decimal
decimal.getcontext().prec = 5
    
def testHourly():
    # Add Budget
    Emperitas = WageCheck(.10, "Emperitas", 40, 15, 4);
    assert_equal(Emperitas.Name, "Emperitas");
    assert_equal(Emperitas.Gross, decimal.Decimal(2400));
    assert_equal(Emperitas.Tax, decimal.Decimal(240));
    assert_equal(Emperitas.Net, decimal.Decimal(2160));
    assert_equal(Emperitas.NumWeeks, 4)
    assert_equal(Emperitas.Hours, 40)
    assert_equal(Emperitas.Wage, 15)
    

def testSalary():
    Army = SalaryCheck(.10, "Army", salary = 4000);
    assert_equal(Army.Gross, decimal.Decimal(4000));
    assert_equal(Army.Name, "Army");
    assert_equal(Army.Tax, decimal.Decimal(400));
    assert_equal(Army.Net, decimal.Decimal(3600));
