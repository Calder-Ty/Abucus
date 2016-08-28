from nose.tools import *
from Abacus.Models import BudgetModel
import decimal
import logging

# Generate Logging file
logging.basicConfig(filename='abucus.log',level = logging.DEBUG)

def test_budget():
    budget = BudgetModel.Budget()
    assert_equal(budget.disposable, 0)
    assert_equal(budget.net, 0)
    assert_equal(budget.gross, 0)
    assert_equal(budget.expenses, {})
    assert_equal(budget.paychecks, {})
    assert_equal(budget.savings, {})

def test_Paychecks():
    # Add Budget
    Emperitas = BudgetModel.Paycheck("Hourly", .10, "Emperitas", 40, 15)
    Army = BudgetModel.Paycheck("Salary", .10, "Army", salary = 4000)
    assert_equal(Emperitas.name, "Emperitas")
    assert_equal(Emperitas.gross, decimal.Decimal(2400))
    assert_equal(Emperitas.tax, decimal.Decimal(240))
    assert_equal(Emperitas.net, decimal.Decimal(2160))
    assert_equal(Army.gross(decimal.Decimal(4000)))


def test_Expense():
    # Add Expense
    pass
