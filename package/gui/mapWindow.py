from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
import folium

from package.service.mapServices import MapServices

class MapWindow(QtWidgets.QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('border : 2px solid black; border-radius: 7px; background-color: #e6e6e6;')

        # Init Map Services
        mapServices = MapServices()

        # Set Layout
        self.setLayout(QtWidgets.QVBoxLayout())

        self.layout().addWidget(mapServices.initMapWidget(self))
        


    



        
