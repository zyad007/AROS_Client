from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *

from package.gui.pages.homePage import HomePage
from package.gui.buttonList import ButtonList

class SideWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Set Layout
        self.setLayout(QVBoxLayout())

        # Add ButtonList
        buttonList = ButtonList(self)
        self.layout().addWidget(buttonList)

        # Set StackedWidget
        self.stackedWidget = QStackedWidget()
        
        homePage = HomePage(self)
        settingsPage = HomePage(self)
        reportPage = HomePage(self)

        self.stackedWidget.addWidget(homePage)
        self.stackedWidget.addWidget(settingsPage)
        self.stackedWidget.addWidget(reportPage)

        self.stackedWidget.setCurrentIndex(0)
        self.layout().addWidget(self.stackedWidget)

        self.setStyleSheet('background-color:white;')
        self.show()

    def setStackIndex(self, i):
        self.stackedWidget.setCurrentIndex(i)

