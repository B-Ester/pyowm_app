from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .weather_api import weather_at_any_city as ws, all_locations, forecast_snow as fs
from .weather_api import clock, cords, forecast as fcs, tomorrow_forecast as tf
from .weather_api import forecast_sun as tfs, forecast_c as fc, forecast_fog as fg
from .weather_api import forecast_h as fh,forecast_t  as ft, weather_at_coords as wac
from .forms import City, Cords
#import ipdb

def index(request):
    return render(request, 'application_pyowm/index.html', {'time': clock()})

def city_forecast(request):
    if request.method == 'POST':
        form = City(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name_of_city']
            context = {
                'data': ws(city_name),
                'city': city_name,
                'cords_lon': cords(city_name).get_lon(),
                'cords_lat': cords(city_name).get_lat(),
                'time': clock()
            }
            return render(request, 'application_pyowm/any_city.html', context)
        else:
            return HttpResponse('Введите корректное назване города')
    else:
        form = City()
        context = {
            'form': form,
            'time': clock()
        }
        return render(request, 'application_pyowm/any_city.html', context)
    return HttpResponseRedirect("/city_forecast/")

def barca(request):
    return render(request, 'application_pyowm/barca.html', {'data': ws(all_locations[5])})

def sever(request):
    return render(request, 'application_pyowm/sever.html', {'data': ws(all_locations[0])})

city1 = 'Severodonetsk'
def forecast(request, city):
    return render(request, 'application_pyowm/any_city.html', {'data': ws(city)})


def future_fc(request):
    if request.method == 'POST':
        form = City(request.POST)
        if form.is_valid():
            city_name = (str(form.cleaned_data['name_of_city']))
            context = {
                'fcst': fcs(city_name),
                'rain': fcs(city_name).will_have_rain(),
                'sun': fcs(city_name).will_have_sun(),
                'snow': fcs(city_name).will_have_snow(),
                'clouds': fcs(city_name).will_have_clouds(),
                'ws': fcs(city_name).most_cold(),
                'cords_lon': cords(city_name).get_lon(),
                'cords_lat': cords(city_name).get_lat(),
                'time': clock(),
                'tom': tf(city_name),
                'tfs': tfs(city_name),
                'fc': fc(city_name),
                'fg': fg(city_name),
                'fs': fs(city_name),
                'fh': fh(city_name),
                'ft': ft(city_name),
                        }
            return render(request, 'application_pyowm/future_fc.html', context)
        else:
            return HttpResponse('Введите корректное назване города')
    else:
        form = City()
        context = {
            'form': form,
            'time': clock()
                    }
    return render(request, 'application_pyowm/future_fc.html', context)
    return HttpResponseRedirect("/future_fc/")

def coords(request):
    if request.method == 'POST':
        form_c = Cords(request.POST)
        if form_c.is_valid():
            long = form_c.cleaned_data['long']
            lat = form_c.cleaned_data['lat']
            res = wac(long, lat).get_weather()
            context = {
                'status': res.get_status(),
                'temp': res.get_temperature('celsius'),
                'humidity': res.get_humidity(),
                'wind': res.get_wind(),
                'press': res.get_pressure(),
                'sr': res.get_sunrise_time(timeformat='iso')[11:19],
                'sn': res.get_sunset_time(timeformat='iso')[11:19],
                'time': clock()
            }
            return render(request, 'application_pyowm/coords.html', context)
        else:
            return HttpResponse('Введите корректные значения координат')
    else:
        form_c = Cords
        context = {
            'form': form_c,
            'time': clock()
        }
        return render(request, 'application_pyowm/coords.html', context)
    return HttpResponseRedirect("/coords/")




