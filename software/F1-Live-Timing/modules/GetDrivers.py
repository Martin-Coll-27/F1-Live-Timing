from ReceiveMaster import ReceiveMasterAPI

class GetDrivers(ReceiveMasterAPI):
    def __init__(self):
        super().__init__()
        self.drivers_URL = 'drivers'

    def getDriversURL(self):
        return self.main_URL + self.drivers_URL + self.session_key
