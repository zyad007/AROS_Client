from PyQt5 import QtGui, QtCore, QtWidgets

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
        settingsPage = HomePage(self)
        reportPage = HomePage(self)

        self.stackedWidget.addWidget(homePage)
        self.stackedWidget.addWidget(settingsPage)
        self.stackedWidget.addWidget(reportPage)

        self.stackedWidget.setCurrentIndex(0)
        self.layout().addWidget(self.stackedWidget)

        self.setStyleSheet('background-color:white;')

    def setStackIndex(self, i):
        self.stackedWidget.setCurrentIndex(i)

    def setNewColor(self):
        self.setStyleSheet('background-color: black;')
        self.show()

