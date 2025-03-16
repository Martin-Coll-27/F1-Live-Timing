class AnalyzeGP():
    def __init__(self):
        self.meeting_name_URL = 'meeting_name'
        self.year_URL = 'year'
        self.session_name_URL = 'session_name'

    def getGPHead(self, data_Meetings, data_Sessions):
        self.session_name = data_Sessions[0][self.session_name_URL]
        self.year = str(data_Meetings[0][self.year_URL])
        self.meeting_name = data_Meetings[0][self.meeting_name_URL]
        return self.session_name + ' ' + self.meeting_name + ' ' + self.year
