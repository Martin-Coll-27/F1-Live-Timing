from ReceiveMaster import ReceiveMasterAPI

class GetLapsURL(ReceiveMasterAPI):
    def __init__(self, driver_number, lap_number):
        super().__init__()
        self.laps_URL = 'laps'
        self.driver_number_URL = '&driver_number='
        self.lap_number_URL = '&lap_number>'
        self.driver_number = str(driver_number)
        self.lap_number = str(lap_number)

    def getURL(self):
        self.general_path = self.main_URL + self.laps_URL + self.session_key
        self.specific_path = self.driver_number_URL + self.driver_number + self.lap_number_URL + self.lap_number
        return self.general_path + self.specific_path
