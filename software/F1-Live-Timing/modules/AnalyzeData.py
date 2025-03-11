class AnalyzeDriversData():
    def setData(self, data):
        self.data = data

    def countDrivers(self):
        cant_drivers = 0
        
        for piloto in self.data:
            cant_drivers += 1
        
        return cant_drivers
     

    def countTeams(self):
        cant_teams = 0
        teams = list()        
        
        for piloto in self.data:
            team = piloto['team_name']
            if team not in teams:
                teams.append(team)
                cant_teams += 1 
        
        return cant_teams
    

    def getDriversList(self):
        drivers_data = list()
        
        for piloto in self.data:
            team = piloto['team_name']
            driver = piloto['name_acronym']
            number = piloto['driver_number']

            drivers_data.append((team, number, driver))
        
        return drivers_data
