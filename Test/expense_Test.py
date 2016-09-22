import decimal;
from nose.tools import *;
from Abacus.Models.expense import Expense;

def percIncomeTest():
    Tithing = Expense("Tithing", percIncome = .1);
    assert_equal(Tithing.percIncome, decimal.Decimal(.1));
    assert_equal(Tithing.name, 'Tithing');

def ammountTest():
    Groceries = BudgetModel.ExpenseItem("Groceries", ammount = 100);
    assert_equal(Groceries.name, "Groceries");
    assert_equal(Groceries.ammount, decimal.Decimal(100));

def printTest():
    Groceries = BudgetModel.ExpenseItem("Groceries", ammount = 100);
    Tithing = Expense("Tithing", percIncome = .1);
    assert_equal(print(Groceries), "Groceries: $100");
    assert_equal(print(Tithing), "Tithing: 10 percent of income");
