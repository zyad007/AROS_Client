from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *


class ButtonList(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.setLayout(QHBoxLayout())
        button_style = '''  border: none;
                 padding: 10px 20px; /* Adjust padding as needed */
                 background-color : rgb(35, 35, 35);
                 color: #fff; /* Set text color */
                 text-decoration: none; /* Remove underline for links */
                 display: inline-block;
                 font-size: 16px; /* Adjust font size as needed */
                 cursor: pointer;
                 border-bottom: 2px solid #ccc; ''' #css code for button style
        homeButton = QPushButton("Home", clicked = lambda: switchToHome())
        settingsButton = QPushButton("Setting", clicked = lambda: switchToSettings())
        reportButton = QPushButton("Report", clicked = lambda: switchToReport())

        self.layout().addWidget(homeButton)
        self.layout().addWidget(settingsButton)
        self.layout().addWidget(reportButton)
        homeButton.setStyleSheet(button_style)
        settingsButton.setStyleSheet(button_style)
        reportButton.setStyleSheet(button_style)
        self.setStyleSheet('background-color: black;')

        def switchToHome():
            parent.setStackIndex(0)

        def switchToSettings():
            parent.setStackIndex(1)
        
        def switchToReport():
            parent.setStackIndex(2)
