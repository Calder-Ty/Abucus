import decimal;
import unittest;
from Abacus.Models.expense import Expense;


class TestExpenseMethods(unittest.TestCase):

    def test_percIncome(self):
        Tithing = Expense("Tithing", percIncome = .1);
        self.assertEqual(Tithing.PercIncome, decimal.Decimal(.1));
        self.assertEqual(Tithing.Name, 'Tithing');

    def test_ammount(self):
        Groceries = Expense("Groceries", ammount = 100);
        self.assertEqual(Groceries.Name, "Groceries");
        self.assertEqual(Groceries.Ammount, decimal.Decimal(100));

    def test_print(self):
        Groceries = Expense(name = "Groceries", ammount = 100);
        Tithing = Expense("Tithing", percIncome = .1);
        self.assertEqual(Groceries.__str__(), "Groceries: $100.00");
        self.assertEqual(Tithing.__str__(), "Tithing: 10.00 percent of income");