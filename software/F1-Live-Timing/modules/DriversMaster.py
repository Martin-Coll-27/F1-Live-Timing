from LapsManager import Laps
from StintsManager import Stints

class Driver(Laps, Stints):
    def __init__(self, information):
        Laps.__init__(self)
        Stints.__init__(self)

        self.team = information[0]
        self.number = information[1]
        self.acronym = information[2] 
        self.lap_number = 0 
        self.stint_number = 0 

    def saveInformation(self):
        prev_lap = list()
        prev_lap.append(self.lap_number)
        prev_lap.append(self.last_lap)
        prev_lap.append(self.last_lap_converted)
        prev_lap.append(self.S1)
        prev_lap.append(self.S2)
        prev_lap.append(self.S3)
        prev_lap.append(self.speed_trap)
        prev_lap.append(self.compound)
        prev_lap.append(self.tyre_age)
        prev_lap.append(self.pit_out)
        self.previous_laps.append(prev_lap)
