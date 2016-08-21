'''
budgetUIController
'''
import importlib.util
from budgetUI import Ui_MainWindow
from PyQt4 import QtCore, QtGui

class budgetUIController(budgetUI.Ui_MainWindow):
    """
    Handles all the stuff to deal with the UI of the budget window
    """

    def __init__(self):
        # Initialize the window
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Test Code just to see if i can get a table to work
        headerLabels = ['Employer','Wages/Salary']
        model = QtGui.QStandardItemModel(2,4)
        model.setHorizontalHeaderLabels(headerLabels)
        self.ui.tableIncome.setModel(model)




if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = budgetUIController
    window.show()

