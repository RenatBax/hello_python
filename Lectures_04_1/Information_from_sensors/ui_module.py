import data_collection as coll
import journal as jour

def temperature_view(sensor):
    data = coll.get_temperature(sensor)
    jour.temperature_logger(data)
    return data

def preassure_view(sensor):
    data = coll.get_preassure(sensor)
    jour.preassure_logger(data)
    return data

def wind_speed_view(sensor):
    data = coll.get_wind_speed(sensor)
    jour.wind_speed_logger(data)
    return data

def data_view(sensor):
    data = coll.data_coll(sensor)
    jour.data_logger(data)
    return data