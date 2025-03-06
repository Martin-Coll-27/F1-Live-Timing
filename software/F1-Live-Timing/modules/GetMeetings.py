from ReceiveMaster import ReceiveMasterAPI

class GetMeetings(ReceiveMasterAPI):
    def __init__(self):
        super().__init__()
        self.meetings_URL = 'meetings'
        
    def getMeetingsURL(self):
        return self.main_URL + self.meetings_URL + self.meeting_key
