# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'budgetUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1, 0))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableIncome = QtGui.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        self.tableIncome.setFont(font)
        self.tableIncome.setObjectName(_fromUtf8("tableIncome"))
        self.gridLayout.addWidget(self.tableIncome, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.labelExpenseTable = QtGui.QLabel(self.centralwidget)
        self.labelExpenseTable.setObjectName(_fromUtf8("labelExpenseTable"))
        self.gridLayout.addWidget(self.labelExpenseTable, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.labelIncomeTable = QtGui.QLabel(self.centralwidget)
        self.labelIncomeTable.setObjectName(_fromUtf8("labelIncomeTable"))
        self.gridLayout.addWidget(self.labelIncomeTable, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtGui.QSpacerItem(20, 170, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.tableView = QtGui.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Sans"))
        self.tableView.setFont(font)
        self.tableView.setMouseTracking(False)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout.addWidget(self.tableView, 1, 1, 4, 1)
        self.labelIncomeTotal = QtGui.QLabel(self.centralwidget)
        self.labelIncomeTotal.setObjectName(_fromUtf8("labelIncomeTotal"))
        self.gridLayout.addWidget(self.labelIncomeTotal, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelExpenseTable.setText(_translate("MainWindow", "TextLabel", None))
        self.labelIncomeTable.setText(_translate("MainWindow", "TextLabel", None))
        self.labelIncomeTotal.setText(_translate("MainWindow", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

