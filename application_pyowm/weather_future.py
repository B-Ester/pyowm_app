import pyowm
import datetime

owm = pyowm.OWM('aa16d2e6e3a3c13b30140edfb4a81b9c', language='ru')
location = str('Severodonetsk')
x = datetime.datetime.now()
fc = owm.daily_forecast(location)

f = fc.get_forecast()
time = "2017-06-13 19:35:00+00"

fc.most_cold()
