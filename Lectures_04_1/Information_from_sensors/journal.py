from datetime import datetime as dt

def temperature_logger(data): 
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('{} - temperature (C): {}\n'
                    .format(time, data))

def preassure_logger(data): 
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('{} - preassure (mmHg): {}\n'
                    .format(time, data))

def wind_speed_logger(data): 
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('{} - wind_speed (m/s): {}\n'
                    .format(time, data))

def data_logger(data): 
    t, p, w = data
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('{} - temperature (C): {}, preassure (mmHg): {}, wind_speed (m/s): {}\n'
                    .format(time, t, p, w))