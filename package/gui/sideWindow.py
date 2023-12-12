from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout , QHBoxLayout , QTextEdit , QSizePolicy , QFrame
from package.gui.pages.homePage import HomePage
from package.gui.buttonList import ButtonList

class SideWindow(QtWidgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Set Layout
        self.setLayout(QtWidgets.QVBoxLayout())

        # Add ButtonList
        buttonList = ButtonList(self)
        self.layout().addWidget(buttonList)

        # Set StackedWidget
        self.stackedWidget = QtWidgets.QStackedWidget()
        
        homePage = HomePage(self)
        settingsPage = QtWidgets.QTabWidget(self)
        reportPage = QtWidgets.QTabWidget(self)

        self.stackedWidget.addWidget(homePage)
        self.stackedWidget.addWidget(settingsPage)
        self.stackedWidget.addWidget(reportPage)










        self.stackedWidget.setCurrentIndex(0)
        self.layout().addWidget(self.stackedWidget)

        self.setStyleSheet('background-color:black;')

    def setStackIndex(self, i):
        self.stackedWidget.setCurrentIndex(i)

    def setNewColor(self):
        self.setStyleSheet('background-color: black;')
        self.show()

