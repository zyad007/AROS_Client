import PyQt5.QtWidgets as pqw
from package.service.userServices import UserServices

class HomePage(pqw.QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        # Init Services
        userServices = UserServices(); 

        # Set Layout
        self.setLayout(pqw.QVBoxLayout())

        # Set Components
        label1 = pqw.QLabel("Hello World!")
        self.layout().addWidget(label1)

        usernameField = pqw.QLineEdit()
        usernameField.setObjectName("username_field")
        usernameField.setText("")
        self.layout().addWidget(usernameField)

        passwordField = pqw.QLineEdit()
        passwordField.setObjectName("password_field")
        passwordField.setText("")
        self.layout().addWidget(passwordField)

        loginButton = pqw.QPushButton("Click", 
        clicked = lambda: loginButtonOnClick())
        self.layout().addWidget(loginButton)

        self.show()

        def loginButtonOnClick():

            username = usernameField.text()
            password = passwordField.text()

            result = userServices.login(username, password)

            if(result == True):
                label1.setText('Logged in')
            else:
                label1.setText('Error')
    