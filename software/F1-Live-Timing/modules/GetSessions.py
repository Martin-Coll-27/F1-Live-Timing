from ReceiveMaster import ReceiveMasterAPI

class GetSessions(ReceiveMasterAPI):
    def __init__(self):
        super().__init__()
        self.sessions_URL = 'sessions'

    def getSessionsURL(self):
        return self.main_URL + self.sessions_URL + self.session_key
