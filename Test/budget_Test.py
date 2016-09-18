from nose.tools import *;
from Abacus.Models import budget;
import decimal;
import logging;

# Generate Logging file
logging.basicConfig(filename='abucus.log', level = logging.DEBUG);

def test_budget():
    bud = budget.Budget();
    assert_equal(bud.disposable, 0);
    assert_equal(bud.net, 0);
    assert_equal(bud.gross, 0);
    assert_equal(bud.expenses, {});
    assert_equal(bud.paychecks, {});
    assert_equal(bud.savings, {});
