import PyQt5.QtWidgets as pqw
from package.service.userServices import UserServices

class HomePage(pqw.QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        # Init Services
        userServices = UserServices(); 

        # Set Layout
        self.setLayout(pqw.QVBoxLayout())

    