class AnalyzeGP():
    def __init__(self):
        self.meeting_name_URL = 'meeting_name'
        self.year_URL = 'year'
        self.session_name_URL = 'session_name'

    def getGPHead(self, data_Meetings, data_Sessions):
        session_name = data_Sessions[0][self.session_name_URL]
        year = str(data_Meetings[0][self.year_URL])
        meeting_name = data_Meetings[0][self.meeting_name_URL]
        return session_name + ' ' + meeting_name + ' ' + year
