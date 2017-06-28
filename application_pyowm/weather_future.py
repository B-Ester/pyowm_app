import pyowm
import datetime

owm = pyowm.OWM('aa16d2e6e3a3c13b30140edfb4a81b9c', language='ru')
location = str('Severodonetsk')
x = datetime.datetime.now()
fc = owm.daily_forecast(location)

f = fc.get_forecast()
time = "2017-06-13 19:35:00+00"

fc.most_cold()
#observation = owm.weather_at_place('Severodonetsk')
#w = observation.get_weather()
#results = w.to_JSON()
#results = w.to_JSON()
#data['temperature_celsius'] = w.get_temperature('celsius')
#data['temperature_fahrenheit'] = w.get_temperature('fahrenheit')
#data['sunrise_time'] = w.get_sunrise_time(timeformat='iso')
#data['sunset_time'] = w.get_sunset_time(timeformat='iso')

def cords(located):
    obs = owm.weather_at_place(str(located))
    l = obs.get_location()
    return l.get_lon(), l.get_lat()