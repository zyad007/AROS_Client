from PyQt5.QtWidgets import QApplication
import sys

from package.gui.mainWindow import MainWindow

def run():
    #init app
    myApp = QApplication(sys.argv)

    #START
    w = MainWindow()
    #END
    
    #exit app
    return myApp.exec_()