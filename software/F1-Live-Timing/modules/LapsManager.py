from GetLaps import GetLapsURL

class Laps(GetLapsURL):
    def __init__(self):
        GetLapsURL.__init__(self)
        self.previous_laps = list()
        

    def findActualLap(self):
        self.setDriverLaps(self.number)
        self.setLastLap(self.lap_number)
        
        lap_URL = self.getLapsURL()
        data = self.receiveData(lap_URL)
        len_data = len(data)

        if(len_data > 0):
            self.lap_number = len_data
    
    
    def lastLapInfo(self): 
        self.setDriverLaps(self.number)
        self.setLastLap(self.lap_number)
        
        lap_URL = self.getLapsURL()
        data = self.receiveData(lap_URL)
        
        if(len(data) > 1):
            try:
                self.pit_out = data['is_pit_out_lap']

                if self.pit_out == 'false':
                    self.last_lap = data['lap_duration']
                    self.S1 = data['duration_sector_1'] 
                    self.S2 = data['duration_sector_2']
                    self.S3 = data['duration_sector_3']
                    self.lap_number += 1
                    self.speed_trap = data['st_speed']
                    self.new_data = 1
                
                else:
                    self.new_data = 0
            
            except:
                return     
        
        else:
            self.new_data = 0


    def convertLaptime(self):
        try:
            minutes = int(self.last_lap // 60)
            seconds = int(self.last_lap % 60)
            miliseconds = round((self.last_lap - minutes * 60 - seconds) * 1000)

            self.last_lap_converted = f'{minutes}:{seconds}.{miliseconds}'
        except:
            return
