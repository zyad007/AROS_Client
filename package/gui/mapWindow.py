from PyQt5 import QtWidgets, QtGui, QtCore

class MapWindow(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        # Set Layout
        self.setLayout(QtWidgets.QVBoxLayout())
        # self.setMinimumWidth(500)

        # Label
        label = QtWidgets.QLabel("Hello")
        label.setStyleSheet('background-color: blue;')

        self.layout().addWidget(label)

        self.show()