"""
Testing Script to Test BudgetModel
"""
import logging
import BudgetModel

# Generate Logging file
logging.basicConfig(filename='../abucus.log',level = logging.DEBUG)

B = BudgetModel.Budget()
count = 0
# Test if adding Paycheck works
B.addPaycheck(Type = "Salary", tax = .1, name = "Emperitas",
              salary = 4000)

if B.gross != 4000:
    logging.debug('Gross should == 4000, Salary is not working')
    count += 1

B.addPaycheck(Type = "Hourly", tax = .1, name = "Army",
              hours = 40, wage = 10, numWeeks = 4)

if B.gross != 5600:
    logging.debug('Gross should == 5600, is the numWeeks setting working?')
    count += 1

if B.net != 5040:
    logging.debug('Net should == 5040, Check the Tax methods')
    count += 1

if B.disposable != 5040:
    logging.debug('Disposable should == 5040, check the budget __init__ method')
    count += 1

B.addExpense('Groceries', B, ammount = 560, maximum = 500)

if B.disposable != 4480:
    logging.debug('disposable should == 4480, does the update method work?')
    count += 1

if B.expenses['Groceries'].percIncome != .1:
    logging.debug('percIncome of Groceries should equal .1, is the percIncome work when a fixed ammount is established?')
    count += 1

B.addSavings('House', B, ammount = 560)

if B.savings['House'].ammount != 560:
    logging.debug('Savings should equal 560, did the add Savings Method work?')
    count += 1

B.addExpense('Pizza', B, percIncome = .1)

if B.expenses['Pizza'].ammount != 560:
    logging.debug('ammount should equal 560 Did the addExpense Work?')
    count += 1

print(count)
