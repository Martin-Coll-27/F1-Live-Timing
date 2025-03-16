from ReceiveMaster import ReceiveMasterAPI

class GetStintsURL(ReceiveMasterAPI):
    def __init__(self):
        super().__init__()
        self.stints_URL = 'stints'    
        self.driver_number_URL = '&driver_number='
        self.stint_number_URL ='&stint_number>'
        self.general_path_stints = self.main_URL + self.stints_URL + self.session_key

    def setDriverStints(self, driver_number):
        self.driver_number = str(driver_number)


    def setLastStint(self, stint_number):
        self.stint_number = str(stint_number)

    
    def getStintsURL(self):
        self.specific_path_stints = self.driver_number_URL + self.driver_number + self.stint_number_URL + self.stint_number
        return self.general_path_stints + self.specific_path_stints
