import unittest;
from Abacus.Models import budget, expense, salaryCheck, savings;
import decimal;
import logging;

decimal.getcontext().prec = 5
# Generate Logging file
logging.basicConfig(filename='abucus.log', level = logging.DEBUG);

class TestBudgetMethods(unittest.TestCase):

    def setUp(self):
        self.bud = budget.Budget();

    def test_budget(self):
        self.assertEqual(self.bud.Disposable, 0);
        self.assertEqual(self.bud.Net, 0);
        self.assertEqual(self.bud.Gross, 0);
        self.assertEqual(self.bud.Expenses, {});
        self.assertEqual(self.bud.Paychecks, {});
        self.assertEqual(self.bud.SavingsDict, {});
    
    def test_addPaycheck(self):
        pay = salaryCheck.SalaryCheck(.1, "Emperitas", 4000);
        self.bud.addPaycheck(pay);
        self.assertEqual(self.bud.Paychecks['Emperitas'], pay);
        self.assertEqual(self.bud.Gross, decimal.Decimal(4000));
        self.assertEqual(self.bud.Net, decimal.Decimal(3600));
        self.assertEqual(self.bud.Disposable, decimal.Decimal(3600));
        self.bud.Paychecks['Emperitas'].drop();

    def test_addExpense(self):
        exp = expense.Expense("Groceries", 200);
        self.assertRaises(Exception, self.bud.addExpense, exp);
        pay = salaryCheck.SalaryCheck(.1, "Emperitas", 4000);
        self.bud.addPaycheck(pay);
        self.bud.addExpense(exp);
        self.assertEqual(self.bud.Disposable, decimal.Decimal(3400));
        self.assertEqual(self.bud.Expenses["Groceries"], expense);
        self.bud.Paychecks['Emperitas'].drop();
        self.bud.Expenses["Groceries"].drop();