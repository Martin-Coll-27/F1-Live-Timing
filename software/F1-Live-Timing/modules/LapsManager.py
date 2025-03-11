from GetLaps import GetLapsURL

class Laps(GetLapsURL):
    def __init__(self):
        GetLapsURL.__init__(self)
        self.previous_laps = list()
        

    def findActualLap(self):
        self.setDriver(self.number)
        self.setLastLap(self.lap_number)
        lap_URL = self.getLapsURL()
        data = self.receiveData(lap_URL)
        len_data = len(data)

        if(len_data > 0):
            self.lap_number = len_data
    
    
    def lastLapInfo(self): 
        self.setLastLap(self.last_lap)
        lap_URL = self.getLapsURL()
        data = self.receiveData(lap_URL)
        
        if(len(data) < 1):
            return
        
        self.last_lap = data['lap_duration']
        self.S1 = data['duration_sector_1'] 
        self.S2 = data['duration_sector_2']
        self.S3 = data['duration_sector_3']
        self.lap_number += 1
        self.speed_trap = data['st_speed']
  

    def convertLaptime(self):
        minutes = int(self.last_lap // 60)
        seconds = int(self.last_lap % 60)
        miliseconds = round((self.last_lap - minutes * 60 - seconds) * 1000)

        self.last_lap_converted = f'{minutes}:{seconds}.{miliseconds}'
