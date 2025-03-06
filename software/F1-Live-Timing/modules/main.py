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

if __name__ == '__main__':
    A = Information()


'''
    C = A.getMeetingsURL()
    D = A.getSessionsURL()
    
    E = A.receiveData(C)
    F = A.receiveData(D)
 
    KKK = A.getGPHead(E,F)
    
    B = A.getURL()
    data = A.receiveData(B)
    A.set_data(data)
    pilotos = A.countDrivers()
    print(pilotos) 
    equipos = A.countTeams()
    print(equipos)
    lista = A.getDriversDict()
    print(lista)    
'''
