import decimal
from nose.tools import *;
from Abacus.Models.savings import Savings;


def ammountTest():
    House = BudgetModel.SavingsItem("House", ammount = 100);
    assert_equal(House.name, "House");
    assert_equal(House.ammount, decimal.Decimal(100));

def percIncomeTest():
    Emergency = BudgetModel.SavingsItem("Emergency", percIncome = .01);
    assert_equal(Emergency.percIncome, decimal.Decimal(.01));
    


