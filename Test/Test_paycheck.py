import unittest;
from Abacus.Models.salaryCheck import SalaryCheck
from Abacus.Models.wageCheck import WageCheck
import decimal
decimal.getcontext().prec = 5


class TestPaycheckMethods(unittest.TestCase):

    def test_hourly(self):
        # Add Budget
        Emperitas = WageCheck(.10, "Emperitas", 40, 15, 4);
        self.assertEqual(Emperitas.Name, "Emperitas");
        self.assertEqual(Emperitas.Gross, decimal.Decimal(2400));
        self.assertEqual(Emperitas.Tax, decimal.Decimal(240));
        self.assertEqual(Emperitas.Net, decimal.Decimal(2160));
        self.assertEqual(Emperitas.NumWeeks, 4)
        self.assertEqual(Emperitas.Hours, 40)
        self.assertEqual(Emperitas.Wage, 15)


    def test_salary(self):
        Army = SalaryCheck(.10, "Army", salary = 4000);
        self.assertEqual(Army.Gross, decimal.Decimal(4000));
        self.assertEqual(Army.Name, "Army");
        self.assertEqual(Army.Tax, decimal.Decimal(400));
        self.assertEqual(Army.Net, decimal.Decimal(3600));
