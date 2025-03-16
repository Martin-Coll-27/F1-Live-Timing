from Information import Information
from DriversMaster import Driver
import time

if __name__ == '__main__':

    GP_Info = Information()
    GP_Info.getSessionHeader()
    print(GP_Info.session_header)    
    Drivers_Tuple_Data = GP_Info.getParticipantsInfo()

    drivers_object_list = list()

    for data in Drivers_Tuple_Data:
        drivers_object_list.append(Driver(data))
        
    drivers_object_manager = tuple(drivers_object_list)

    for driver in drivers_object_manager:
#        driver.findActualStint()
#        driver.findActualLap()
        print(driver.acronym)
'''
    while True:
        for driver in drivers_object_manager:
            if driver.acronym == 'BOR':
#                driver.findActualStint()
                driver.findActualLap()

                try:
                    driver.lastLapInfo()
                except:
                    continue
                print(driver.new_data)
                if driver.new_data == 1:
                    driver.convertLaptime()
#                    if driver.pit_out == 'true':
#                        driver.lastStintInfo()
                        
#                    elif driver.pit_out == 'false': 
#                        driver.addTyreAge()
                    
                    print(driver.lap_number)
                    print(driver.last_lap)
                    print(driver.last_lap_converted)
                    print(driver.S1)
                    print(driver.S2)
                    print(driver.S3)
                    print(driver.speed_trap)
#                    print(driver.compound)
#                    print(driver.tyre_age)
                    print(driver.pit_out)
               
                time.sleep(5)
'''             
