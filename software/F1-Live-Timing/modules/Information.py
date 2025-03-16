from GetDrivers import GetDrivers
from AnalyzeData import AnalyzeDriversData
from GetMeetings import GetMeetings
from GetSessions import GetSessions
from AnalyzeGP import AnalyzeGP

class Information(GetSessions, GetMeetings, AnalyzeGP, GetDrivers, AnalyzeDriversData):
    def __init__(self):
        GetMeetings.__init__(self)
        GetSessions.__init__(self)
        GetDrivers.__init__(self)
        AnalyzeDriversData.__init__(self)
        AnalyzeGP.__init__(self)


    def getSessionHeader(self):
        meeting_URL = self.getMeetingsURL()
        session_URL = self.getSessionsURL()
    
        meeting_data = self.receiveData(meeting_URL)
        session_data = self.receiveData(session_URL)
 
        self.session_header = self.getGPHead(meeting_data, session_data)

    
    def getParticipantsInfo(self):
        drivers_URL = self.getDriversURL()
        drivers_data = self.receiveData(drivers_URL)
        self.setData(drivers_data)

        self.drivers_num = self.countDrivers()
        self.teams_num = self.countTeams()
    
        drivers_tuple = self.getDriversTuple()
        return drivers_tuple
