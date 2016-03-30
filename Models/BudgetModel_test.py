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
    logging.debug("Gross should == 4000")
    count += 1

B.addPaycheck(Type = "Hourly", tax = .1, name = "Emperitas",
              hours = 40, wage = 10)

if B.gross != 5600:
    logging.debug('Gross should == 5600')
    count += 1

if B.net != 5040:
    logging.debug('Net should == 5040')
    count += 1

if B.disposable != 5600:
    logging.debug('Disposable == 5600')
    count += 1

B.addExpense('Groceries', B, ammount = 560, maximum = 500)

if B.disposable != 5040:
    logging.debug('Expenses == 5040')
    count += 1

if B.expenses['Groceries'].percIncome != .1:
    logging.debug('percIncome of Groceries should equal .1')
    count += 1

B.addSavings('House', B, ammount = 560)

if B.savings['House'].ammount != 560:
    logging.debug('Savings should equall 560')
    count += 1

B.addExpense('Pizza', B, percIncome = .1)

if B.expenses['Pizza'].ammount == 560:
    logging.debug('ammount should equal 560')
    count += 1

print(count)
