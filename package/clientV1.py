from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel, QVBoxLayout, QDesktopWidget , QDialog
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl, QTimer 
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
import folium

class GPSMapApp(QWidget):
    def __init__(self):
        super().__init__()

        self.latitude_input = QLineEdit(self)
        self.longitude_input = QLineEdit(self)
        self.generate_button = QPushButton("Generate Map", self)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Latitude:", self))
        layout.addWidget(self.latitude_input)

        layout.addWidget(QLabel("Longitude:", self))
        layout.addWidget(self.longitude_input)

        layout.addWidget(self.generate_button)
        self.generate_button.clicked.connect(self.generate_map)

    def generate_map(self):
        
        latitude = float(self.latitude_input.text())
        longitude = float(self.longitude_input.text())

       
        map_center = [latitude, longitude]
        map_object = folium.Map(location=map_center, zoom_start=15)
        folium.Marker(location=map_center, popup='Your Location').add_to(map_object)
        road_problem_coords = [
            {"lat": 30.001220 , "lon": 31.167195, "description": "Road Closure"},
            {"lat": 30.002614 , "lon": 31.170725, "description": "Pothole"},
           
            ]

        for problem in road_problem_coords:
            road_problem_location = [problem["lat"], problem["lon"]]
            folium.Marker(
                location=road_problem_location,
                popup=folium.Popup(problem["description"], parse_html=True),
                icon=folium.Icon(color="red")
            ).add_to(map_object)    
       
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(current_dir, "generated_map.html")
        map_object.save(html_path)

        
        new_window = GPSMapViewer(html_path)
        new_window.setGeometry(100, 100, 800, 600)  
        new_window.exec_()

    def update_coordinates(self, latitude, longitude):
        self.latitude_input.setText(str(latitude))
        self.longitude_input.setText(str(longitude))

class GPSMapViewer(QDialog):
    def __init__(self, html_file):
        super().__init__()

        self.map_view = QWebEngineView(self)
        self.map_view.setUrl(QUrl.fromLocalFile(html_file))

        layout = QVBoxLayout(self)
        layout.addWidget(self.map_view)
        self.setWindowTitle("Map Viewer")
     
class MainWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        uic.loadUi(utils.PATH('../ui/MainWindow.ui'), self)
        self.setWindowTitle("Main Window")
        # self.setWindowIcon(QIcon("D:\\Valeo GradProj\\ios-car-3.png"))
        button_MAP = self.findChild(QPushButton, 'pushButton')
        button_Setting = self.findChild(QPushButton, 'pushButton_2')
        button_Help = self.findChild(QPushButton, 'pushButton_3')
        self.username = username
        button_MAP.clicked.connect(self.clicked_MAP)
        self.map_window = None
    def clicked_MAP(self):
         self.map_window = GPSMapApp()
         self.map_window.show()
         self.close()

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(utils.PATH('../ui/login.ui'), self)  # Load the Qt Designer UI file

        # Find the button and line edit
        button = self.findChild(QPushButton, 'pushButton')
        self.userName = self.findChild(QLineEdit, 'lineEdit')
        self.password = self.findChild(QLineEdit, 'lineEdit_2')

        # Connect the button click event to the method
        button.clicked.connect(self.clicked_btn)

        # Set window properties
        self.setWindowTitle("AROS")
        # self.setWindowIcon(QIcon("D:\\Valeo GradProj\\ios-car-3.png"))

        self.main_window = None

    def clicked_btn(self):
        uname = self.userName.text()
        passwrd = self.password.text()

        if uname == "admin" and passwrd == "admin":

            self.main_window = MainWindow(uname)
            self.main_window.show()
            self.close()
        else:
            success_box = QMessageBox(self)
            success_box.setIcon(QMessageBox.Information)
            success_box.setWindowTitle("Login Failed")
            success_box.setText("Login Failed!")
            success_box.setStyleSheet('background-color:  rgb(35, 35, 35); color: white;')
            success_box.addButton(QMessageBox.Ok)
            success_box.exec_()


