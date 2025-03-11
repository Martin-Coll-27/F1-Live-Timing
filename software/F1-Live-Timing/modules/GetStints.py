from ReceiveMaster import ReceiveMasterAPI

class GetStintsURL(ReceiveMasterAPI):
    def __init__(self):
        super().__init__()
        self.stints_URL = 'stints'    
        self.driver_number_URL = '&driver_number='
        self.stint_number_URL ='&stint_number>'


    def setDriver(self, driver_number):
        self.driver_number = str(driver_number)


    def setLastStint(self, stint_number):
        self.stint_number = str(stint_number)

    
    def getStintsURL(self):
        self.general_path = self.main_URL + self.stints_URL + self.session_key
        self.specific_path = self.driver_number_URL + self.driver_number + self.stint_number_URL + self.stint_number
        return self.general_path + self.specific_path
