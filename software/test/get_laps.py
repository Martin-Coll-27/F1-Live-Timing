from urllib.request import urlopen
import json

response = urlopen('https://api.openf1.org/v1/laps?session_key=latest&driver_number=44')

data = json.loads(response.read().decode('utf-8'))
print(data)
