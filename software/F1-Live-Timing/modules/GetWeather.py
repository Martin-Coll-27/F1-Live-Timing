from ReceiveMaster import ReceiveMasterAPI

class GetWeatherURL(ReceiveMasterAPI):
    def __init__(self, date):
        super().__init__()
        self.weather_URL = 'weather'
        self.date_URL = '&date>'
        self.date = date

    def getURL(self): 
        return self.main_URL + self.weather_URL + self.session_key + self.date_URL + self.date
