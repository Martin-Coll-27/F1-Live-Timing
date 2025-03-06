from urllib.request import urlopen
import json

response = urlopen('https://api.openf1.org/v1/sessions?session_key=latest')
data = json.loads(response.read().decode('utf-8'))
print(data)

