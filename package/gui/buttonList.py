from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *


class ButtonList(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.setLayout(QHBoxLayout())

        homeButton = QPushButton("Home", clicked = lambda: switchToHome())
        settingsButton = QPushButton("Setting", clicked = lambda: switchToSettings())
        reportButton = QPushButton("Report", clicked = lambda: switchToReport())

        self.layout().addWidget(homeButton)
        self.layout().addWidget(settingsButton)
        self.layout().addWidget(reportButton)

        self.setStyleSheet('background-color: red;')
        self.show()

        def switchToHome():
            parent.setStackIndex(0)

        def switchToSettings():
            parent.setStackIndex(1)
        
        def switchToReport():
            parent.setStackIndex(2)
