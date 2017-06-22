import pyowm, json
import datetime

owm = pyowm.OWM('aa16d2e6e3a3c13b30140edfb4a81b9c', language='ru')

def weather_at_any_city(located):
    observation = owm.weather_at_place(located)
    w = observation.get_weather()
    results = w.to_JSON()
    data = json.loads(results)
    data['temperature_celsius'] = w.get_temperature('celsius')
    data['temperature_fahrenheit'] = w.get_temperature('fahrenheit')
    data['sunrise_time'] = w.get_sunrise_time(timeformat='iso')[11:19]
    data['sunset_time'] = w.get_sunset_time(timeformat='iso')[11:19]
    return data

time_now = str(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

all_locations = ['Severodonetsk', 'Kiev', 'Kharkov', 'Lvov', 'Odessa', 'Barcelona',  'London', 'Madrid', 'Paris', 'Berlin', 'Lissabon']
#observation = owm.weather_at_place('Severodonetsk')
#w = observation.get_weather()
#results = w.to_JSON()
#results = w.to_JSON()
#data['temperature_celsius'] = w.get_temperature('celsius')
#data['temperature_fahrenheit'] = w.get_temperature('fahrenheit')
#data['sunrise_time'] = w.get_sunrise_time(timeformat='iso')
#data['sunset_time'] = w.get_sunset_time(timeformat='iso')












