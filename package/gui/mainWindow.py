from PyQt5 import QtWidgets, QtGui, QtCore
import time

from package.gui.sideWindow import SideWindow
from package.service.userServices import UserServices
from package.service.mapServices import MapServices 
from package.gui.mapWindow import MapWindow



class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Init Services
        userServices = UserServices(); 

        # Config Window
        self.setWindowTitle('AROS - Auto Reporitng Obstacle')

        # Get the screen dimensions
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        screen_width, screen_height = screen.width(), screen.height()

        # Set layout
        self.setLayout(QtWidgets.QHBoxLayout())


        sideWindow = SideWindow(self)
        mapWindow = MapWindow(self)

        sideWindow.setFixedWidth(screen_width//4)

        self.layout().addWidget(sideWindow)
        self.layout().addWidget(mapWindow)

        self.showMaximized()