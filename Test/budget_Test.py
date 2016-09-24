from nose.tools import *;
from Abacus.Models import budget;
import decimal;
import logging;

# Generate Logging file
logging.basicConfig(filename='abucus.log', level = logging.DEBUG);

def test_budget():
    bud = budget.Budget();
    assert_equal(bud.Disposable, 0);
    assert_equal(bud.Net, 0);
    assert_equal(bud.Gross, 0);
    assert_equal(bud.Expenses, {});
    assert_equal(bud.Paychecks, {});
    assert_equal(bud.SavingsDict, {});
