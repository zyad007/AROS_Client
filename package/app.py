from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
import sys
import time
import threading

from package.gui.mainWindow import MainWindow
from package.service.mapServices import MapServices

def run():
    #init app
    myApp = QApplication(sys.argv)

    #START
    w = MainWindow()
    #END
    
    #exit app
    return myApp.exec_()