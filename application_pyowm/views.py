from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .weather_api import weather_at_any_city as ws, all_locations, forecast_snow as fs
from .weather_api import cords, tomorrow_forecast as tf
from .weather_api import forecast_sun as tfs, forecast_c as fc, forecast_fog as fg
from .weather_api import forecast_h as fh, forecast_t as ft, weather_at_coords as wac
from .forms import City, Cords
from .weather_api import timezone_detec as tzdt, time_in_tz_now as titn

def index(request):
    context = {
        'loc': all_locations,
     }
    return render(request, 'application_pyowm/index.html', context)

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
                'location': all_locations,
                'tz': tzdt(city_name),
                'titin': titn(tzdt(city_name))[10:19],
            }
            return render(request, 'application_pyowm/any_city.html', context)
        else:
            return HttpResponse('Введите корректное назване города')
    else:
        form = City()
        context = {
            'form': form,
        }
        return render(request, 'application_pyowm/any_city.html', context)
    return HttpResponseRedirect("/city_forecast/")

def city_from_loc(request):
    context = {
        'data': ws(),
        'city': all_locations,
        'cords_lon': cords().get_lon(),
        'cords_lat': cords().get_lat(),
        'location': all_locations
    }
    return render(request, 'application_pyowm/any_city.html', all_locations, context)


def forecast(request, city):
    context = {
        'loc': all_locations,
        'data': ws(str(city))
    }
    return render(request, 'application_pyowm/any_city.html', context, city)

def future_fc(request):
    if request.method == 'POST':
        form = City(request.POST)
        if form.is_valid():
            city_name = (str(form.cleaned_data['name_of_city']))
            context = {
                'cords_lon': cords(city_name).get_lon(),
                'cords_lat': cords(city_name).get_lat(),
                'tom': tf(city_name),
                'tfs': tfs(city_name),
                'fc': fc(city_name),
                'fg': fg(city_name),
                'fs': fs(city_name),
                'fh': fh(city_name),
                'ft': ft(city_name),
                'city': city_name
                        }
            return render(request, 'application_pyowm/future_fc.html', context)
        else:
            return HttpResponse('Введите корректное назване города')
    else:
        form = City()
        context = {
            'form': form,
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
                'long': long,
                'lat': lat
            }
            return render(request, 'application_pyowm/coords.html', context)
        else:
            return HttpResponse('Введите корректные значения координат (0-90)')
    else:
        form_c = Cords
        context = {
            'form': form_c,
        }
        return render(request, 'application_pyowm/coords.html', context)
    return HttpResponseRedirect("/coords/")

def sever(request):
    city_name ='Severodonetsk'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def kiev(request):
    city_name ='Kiev'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def kharkov(request):
    city_name ='Kharkov'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def lvov(request):
    city_name ='Lvov'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def dnepr(request):
    city_name ='Dnerpopetrovsk'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def odessa(request):
    city_name ='Odessa'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def barca(request):
    city_name ='Barcelona'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def london(request):
    city_name ='London'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def paris(request):
    city_name ='Paris'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def madrid(request):
    city_name ='Madrid'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def berlin(request):
    city_name ='Berlin'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)

def lissabon(request):
    city_name ='Lissabon'
    context = {
        'data': ws(city_name),
        'city': city_name,
        'cords_lon': cords(city_name).get_lon(),
        'cords_lat': cords(city_name).get_lat(),
        'location': all_locations,
        'tz': tzdt(city_name),
        'titin': titn(tzdt(city_name))[10:19],
    }
    return render(request, 'application_pyowm/any_city.html', context)





