import PyQt5.QtWidgets as pqw
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor
from package.service.userServices import UserServices

class HomePage(pqw.QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        # Init Services
        userServices = UserServices()

        # Create a QLabel for notifications
        notifications_label = pqw.QLabel("Notifications", self)
        
        # Apply style sheet for styling
        notifications_label.setStyleSheet('font-size: 16px; font-weight: bold; font-style: italic; color: white;')

        # Create a QTextEdit (large text box)
        self.textbox = pqw.QTextEdit(self)
        self.textbox.setReadOnly(True)  # Make the QTextEdit read-only
        self.textbox.setStyleSheet('background-color: white;')  # Set white background

        # Set the size policy to Expanding so that the text box takes available space
        self.textbox.setSizePolicy(pqw.QSizePolicy.Expanding, pqw.QSizePolicy.Expanding)

        # Set a minimum height for the text box (optional)
        self.textbox.setMinimumHeight(100)

        # Create a QVBoxLayout to organize the widgets vertically
        layout = pqw.QVBoxLayout(self)

        # Add the notifications label to the layout
        layout.addWidget(notifications_label)

        # Add the text box to the layout
        layout.addWidget(self.textbox)

        # Set the layout of the HomePage
        self.setLayout(layout)
        self.updateWarning("Accident 50m away")
        self.updateMessage("ID101-Speed=50km/h")

    def updateWarning(self, warning_text):
        # Set red color for warning text
        warning_color = QColor("red")

    # Add a newline character before each new warning
        if self.textbox.toPlainText():  # Add a newline only if there's existing text
         warning_text = '\n' + '>>Warning: ' + warning_text
        else:  # Prepend '>>' only to the first line
            warning_text = '>>Warning: ' + warning_text

    # Move the cursor to the end
        cursor = self.textbox.textCursor()
        cursor.movePosition(QTextCursor.End)

    # Set the text color and font size for the inserted text
        char_format = QTextCharFormat()
        char_format.setForeground(warning_color)
        char_format.setFontPointSize(16)  # Set the font size to 16

        cursor.mergeCharFormat(char_format)
        cursor.insertText(warning_text)

        cursor.movePosition(QTextCursor.End)

    # Set the updated cursor
        self.textbox.setTextCursor(cursor)

    def updateMessage(self, message_text):
    # Set green color for message text
        message_color = QColor("green")

    # Add a newline character before each new message
        if self.textbox.toPlainText():  # Add a newline only if there's existing text
            message_text = '\n' + '>>Message: ' + message_text
        else:  # Prepend '>>' only to the first line
            message_text = '>>Message: ' + message_text

         # Move the cursor to the end
        cursor = self.textbox.textCursor()
        cursor.movePosition(QTextCursor.End)

        # Set the text color and font size for the inserted text
        char_format = QTextCharFormat()
        char_format.setForeground(message_color)
        char_format.setFontPointSize(16)  # Set the font size to 16

        cursor.mergeCharFormat(char_format)
        cursor.insertText(message_text)

        cursor.movePosition(QTextCursor.End)

         # Set the updated cursor
        self.textbox.setTextCursor(cursor)