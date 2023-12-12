import os
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QTextEdit, QWidget, QDesktopWidget, QSizePolicy
from PyQt5.QtGui import QPixmap, QColor, QTextCursor, QTextCharFormat
from package.service.userServices import UserServices
from PyQt5.QtCore import Qt

class ImagePopupDialog(QDialog):
    def __init__(self, parent, title, image_path):
        super().__init__(parent)
        self.setWindowTitle(title)

        image_label = QLabel(self)
        pixmap = QPixmap(image_path)

        # Increase the width of the image
        pixmap = pixmap.scaledToWidth(400, Qt.SmoothTransformation)
        image_label.setPixmap(pixmap)

        warning_label = QLabel("Warning", self)
        warning_label.setAlignment(Qt.AlignCenter)
        warning_label.setStyleSheet('color: white;')

        accept_button = QPushButton('Accept', self)
        accept_button.clicked.connect(self.accept_warning)
        accept_button.setStyleSheet('background-color: white;')

        reject_button = QPushButton('Reject', self)
        reject_button.clicked.connect(self.reject_warning)
        reject_button.setStyleSheet('background-color: white;')

        layout = QVBoxLayout(self)
        layout.addWidget(image_label)
        layout.addWidget(warning_label)
        layout.addWidget(accept_button)
        layout.addWidget(reject_button)

        self.setLayout(layout)
        self.resize(500, 500)
        self.center_on_screen()
        self.result = None

    def accept_warning(self):
        self.result = True
        self.accept()

    def reject_warning(self):
        self.result = False
        self.reject()

    def center_on_screen(self):
        screen_geometry = QDesktopWidget().screenGeometry()
        center_point = screen_geometry.center()
        self.move(center_point - self.rect().center())

class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        userServices = UserServices()

        notifications_label = QLabel("Notifications", self)
        notifications_label.setStyleSheet('font-size: 16px; font-weight: bold; font-style: italic; color: white;')

        self.textbox = QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setStyleSheet('background-color: white;')
        self.textbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.textbox.setMinimumHeight(100)

        layout = QVBoxLayout(self)
        layout.addWidget(notifications_label)
        layout.addWidget(self.textbox)

        self.setLayout(layout)
        #if recived obstacle for AI model
        self.updateWarning("obstacle away")
        self.updateImagePopup("D:\Valeo GradProj\obstacle.jpg")

    def show_image_popup(self, title, image_path):
        # Create and show the image popup dialog with the main window as the parent
        image_popup = ImagePopupDialog(self, title, image_path)
        image_popup.setFixedSize(400, 400)
        image_popup.center_on_screen()
        image_popup.show()
        if image_popup.result == True:
            print("true")
            image_popup.close()
        elif image_popup.result == False:
            print("False")
            image_popup.close()

    def updateImagePopup(self, image_path):
        self.show_image_popup('Image Popup', image_path)
    def updateWarning(self, warning_text):
        # Set red color for warning text
        warning_color = QColor("red")

        # Add a newline character before each new warning
        if self.textbox.toPlainText():  # Add a newline only if there's existing text
            warning_text = '\n' + '>>' + warning_text
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

        # Add a newline character before each new warning
        if self.textbox.toPlainText():  # Add a newline only if there's existing text
            message_text = '\n' + '>>' + message_text
        else:  # Prepend '>>' only to the first line
            message_text = '>>' + message_text

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
    