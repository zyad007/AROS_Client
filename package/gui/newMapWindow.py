import time
from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets

from package.service.mapServices import MapServices
from package.utils.Obstacle import Obstacle

class MapWindow(QtWidgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('border : 2px solid black; border-radius: 7px; background-color: #e6e6e6;')

        # Init Map Services
        mapServices = MapServices()

        # Set Layout
        self.setLayout(QtWidgets.QVBoxLayout())

        self.mapWidget = mapServices.initMapWidget(self)

        self.layout().addWidget(self.mapWidget)

        mapServices.addObstacle(obstacle=Obstacle(30.001220, 31.167195, "rock"))

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.rerenderMap)
        self.timer.start()
    
    def rerenderMap(self):
        m = MapServices()
        m.rerenderMapWidget()