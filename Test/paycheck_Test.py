from nose.tools import *;
from Abacus.Models.paycheck import Paycheck;
import decimal
    
def testHourly():
    # Add Budget
    Emperitas = Paycheck("Hourly", .10, "Emperitas", 40, 15);
    assert_equal(Emperitas.name, "Emperitas");
    assert_equal(Emperitas.gross, decimal.Decimal(2400));
    assert_equal(Emperitas.tax, decimal.Decimal(240));
    assert_equal(Emperitas.net, decimal.Decimal(2160));
    

def testSalary():
    Army = Paycheck("Salary", .10, "Army", salary = 4000);
    assert_equal(Army.gross, decimal.Decimal(4000));
    assert_equal(Army.name, "Army");
    assert_equal(Army.gross, decimal.Decimal(4000));
    assert_equal(Army.tax, decimal.Decimal(400));
    assert_equal(Army.net, decimal.Decimal(3600));
