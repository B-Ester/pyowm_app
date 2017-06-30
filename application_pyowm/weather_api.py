import pyowm, json, datetime

owm = pyowm.OWM('aa16d2e6e3a3c13b30140edfb4a81b9c', language='ru')

all_locations = ['Severodonetsk', 'Kiev', 'Kharkov', 'Lvov', 'Odessa', 'Barcelona',  'London', 'Madrid', 'Paris', 'Berlin', 'Lissabon']

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

def clock():
    tcp = datetime.datetime.now()
    return tcp

def cords(located):
    obs = owm.weather_at_place(str(located))
    cords = obs.get_location()
    return cords

def forecast(located):
    fc = owm.daily_forecast(located, limit=2)
    return fc

time_tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
hours = datetime.datetime.today().hour
min = datetime.datetime.today().minute
sec = datetime.datetime.today().second
time_00 = time_tomorrow - datetime.timedelta(hours=hours, minutes=min, seconds=sec)
time_07 = time_00 + datetime.timedelta(hours=7)
time_12 = time_00 + datetime.timedelta(hours=12)
time_16 = time_00 + datetime.timedelta(hours=16)
time_21 = time_00 + datetime.timedelta(hours=21)
all_time = [time_07, time_12, time_16, time_21]

def tomorrow_forecast(located):
    fc = owm.daily_forecast(located)
    return fc.will_be_rainy_at(all_time[0]), fc.will_be_rainy_at(all_time[1]), fc.will_be_rainy_at(all_time[2]), fc.will_be_rainy_at(all_time[3])

def forecast_sun(located):
    fc = owm.daily_forecast(located)
    return fc.will_be_sunny_at(all_time[0]), fc.will_be_sunny_at(all_time[1]), fc.will_be_sunny_at(all_time[2]), fc.will_be_sunny_at(all_time[3])

def forecast_c(located):
    fc = owm.daily_forecast(located)
    return fc.will_be_cloudy_at(all_time[0]), fc.will_be_cloudy_at(all_time[1]), fc.will_be_cloudy_at(all_time[2]), fc.will_be_cloudy_at(all_time[3])

def forecast_fog(located):
    fc = owm.daily_forecast(located)
    return fc.will_be_foggy_at(all_time[0]), fc.will_be_foggy_at(all_time[1]), fc.will_be_foggy_at(all_time[2]), fc.will_be_foggy_at(all_time[3])

def forecast_snow(located):
    fc = owm.daily_forecast(located)
    return fc.will_be_snowy_at(all_time[0]), fc.will_be_snowy_at(all_time[1]), fc.will_be_snowy_at(all_time[2]), fc.will_be_snowy_at(all_time[3])

def forecast_h(located):
    fc = owm.daily_forecast(located)
    return fc.will_be_hurricane_at(all_time[0]), fc.will_be_hurricane_at(all_time[1]), fc.will_be_hurricane_at(all_time[2]), fc.will_be_hurricane_at(all_time[3])

def forecast_t(located):
    fc = owm.daily_forecast(located)
    return fc.will_be_tornado_at(all_time[0]), fc.will_be_tornado_at(all_time[1]), fc.will_be_tornado_at(all_time[2]), fc.will_be_tornado_at(all_time[3])

def weather_at_coords(long, lat):
    obs = owm.weather_at_coords(long, lat)
    return obs