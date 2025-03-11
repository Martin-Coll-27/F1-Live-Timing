from GetStints import GetStintsURL

class Stints(GetStintsURL):
    def __init__(self):
        GetStintsURL.__init__(self)


    def findActualStint(self):
        self.setDriver(self.number)
        self.setLastStint(self.stint_number)
        stint_URL = self.getStintsURL()
        data = self.receiveData(stint_URL)
        len_data = len(data)

        if(len_data > 0):
            self.stint_number = len_data
    
    
    def lastStintInfo(self): 
        self.setLastStint(self.stint_number)
        stint_URL = self.getStintsURL()
        data = self.receiveData(stint_URL)
        
        if(len(data) < 1):
            return
        
        self.compound = data['compound']
        self.tyre_age = data['tyre_age_at_start'] 
        self.stint_number += 1

    def addTyreAge(self):
        self.tyre_age += 1
