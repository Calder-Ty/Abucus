from nose.tools import *
from Abacus.Models import BudgetModel
import logging

# Generate Logging file
logging.basicConfig(filename='abucus.log',level = logging.DEBUG)

def test_addPaycheck():
    # Add Budget
    budget = BudgetModel.Budget()
    budget.ad


def setup():
    print("Setup!")

def teardown():
    print("Tear Down")

def test_basic():
    print("I Ran basic Test!")

