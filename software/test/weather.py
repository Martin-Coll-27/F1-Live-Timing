from urllib.request import urlopen
import json
import time

response = urlopen('https://api.openf1.org/v1/weather?session_key=latest')
data = json.loads(response.read().decode('utf-8'))

num_datos = len(data) - 1

ult_dato = data[num_datos]

print(ult_dato)

while True:
    url = 'https://api.openf1.org/v1/weather?session_key=latest&date>' + ult_dato['date']
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    
    try:
        actual_dato = data[0]
    except:
        continue
    
    if actual_dato != ult_dato:
        print(data)
        ult_dato = actual_dato
    time.sleep(30)
