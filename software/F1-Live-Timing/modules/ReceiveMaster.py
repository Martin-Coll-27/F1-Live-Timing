from abc import ABC, abstractmethod
from urllib.request import urlopen
import json

class ReceiveMasterAPI(ABC):
    def __init__(self):
        self.main_URL = 'https://api.openf1.org/v1/'
        self.session_key = '?session_key=latest'
        self.meeting_key = '?meeting_key=latest'

    def receiveData(self, URL):
        response = urlopen(URL)
        return json.loads(response.read().decode('utf-8'))
