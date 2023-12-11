import folium
import io
from PyQt5 import QtWebEngineWidgets

from package.service.singletonMeta import SingletonMeta


class MapServices(metaclass= SingletonMeta):
    
    def __init__(self):
        self.mapWidget: QtWebEngineWidgets.QWebEngineView = None
        self.obstacles = [{"lat": 30.001220 , "lng": 31.167195, "description": "Road Closure"}]  # { lat:float, lng:float, description:str }

    def initMapWidget(self, parent):
        lat, lng = self.__getLocation()
        mapHTML = self.__renderMapHTML([lat, lng])
        w = QtWebEngineWidgets.QWebEngineView(parent)
        w.setHtml(mapHTML)
        return w



    #GPS Module Interfacing Logic
    def __getLocation(self):
        lat = 30.001220
        lng = 31.167195
        return lat, lng
    

    def __renderMapHTML(self, center):
        mapObject = folium.Map( center, zoom_start= 20)
        data = io.BytesIO()

        # Load Obstacles Location
        for obstacle in self.obstacles:
            lat, lng = obstacle["lat"], obstacle["lng"]
            description = obstacle["description"]
            folium.Marker(
                location= [lat, lng],
                popup= folium.Popup( description , parse_html=True),
                icon= folium.Icon(color='red')
            ).add_to(mapObject)

        mapObject.save(data, close_file=False)
        return data.getvalue().decode()
