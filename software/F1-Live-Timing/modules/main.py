from Information import Information
from DriversMaster import Driver

Drivers_List_Data = [('Red Bull Racing', 1, 'VER'), ('McLaren', 4, 'NOR'), ('Kick Sauber', 5, 'BOR'), ('Racing Bulls', 6, 'HAD'), ('Alpine', 7, 'DOO'), ('Alpine', 10, 'GAS'), ('Mercedes', 12, 'ANT'), ('Aston Martin', 14, 'ALO'), ('Ferrari', 16, 'LEC'), ('Aston Martin', 18, 'STR'), ('Racing Bulls', 22, 'TSU'), ('Williams', 23, 'ALB'), ('Kick Sauber', 27, 'HUL'), ('Haas F1 Team', 31, 'OCO'), ('Ferrari', 44, 'HAM'), ('Mercedes', 63, 'RUS'), ('McLaren', 81, 'PIA'), ('Haas F1 Team', 87, 'BEA')]   

if __name__ == '__main__':
    GP_Info = Information()

    GP_Info.getSessionHeader()
    print(GP_Info.session_header)    

    Drivers_List_Data = GP_Info.getParticipantsInfo()


    drivers_object_list = list()

    for data in Drivers_List_Data:
        drivers_object_list.append(Driver(data))
        
    drivers_object_manager = tuple(drivers_object_list)

    for driver in drivers_object_manager:
        driver.findActualStint()
        driver.findActualLap()
   
    for driver in drivers_object_manager:
        print(driver.acronym)
        print(driver.stint_number)
        print(driver.lap_number)
        print('\n')
    
