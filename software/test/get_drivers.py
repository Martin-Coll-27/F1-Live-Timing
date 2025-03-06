from urllib.request import urlopen
import json

response = urlopen('https://api.openf1.org/v1/drivers?session_key=latest')
data = json.loads(response.read().decode('utf-8'))

for piloto in data:
    print('Piloto:', piloto['name_acronym'], '-- Número:', piloto['driver_number'], '-- Equipo:', piloto['team_name'])
