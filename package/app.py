from PyQt5.QtWidgets import QApplication, QWidget
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