import unittest;
from Abacus.Models import budget;
import decimal;
import logging;

# Generate Logging file
logging.basicConfig(filename='abucus.log', level = logging.DEBUG);

class TestBudgetMethods(unittest.TestCase):
    
    def test_budget(self):
        bud = budget.Budget();
        self.assertEqual(bud.Disposable, 0);
        self.assertEqual(bud.Net, 0);
        self.assertEqual(bud.Gross, 0);
        self.assertEqual(bud.Expenses, {});
        self.assertEqual(bud.Paychecks, {});
        self.assertEqual(bud.SavingsDict, {});