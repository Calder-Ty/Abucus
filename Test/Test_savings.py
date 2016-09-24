import decimal
import unittest;
from Abacus.Models.savings import Savings;


class TestSavingsMethods(unittest.TestCase):

    def test_ammount(self):
        House = Savings("House", ammount = 100);
        self.assertEqual(House.Name, "House");
        self.assertEqual(House.Ammount, decimal.Decimal(100));

    def test_percIncome(self):
        Emergency = Savings("Emergency", percIncome = .01);
        self.assertEqual(Emergency.PercIncome, decimal.Decimal(.01));
        


