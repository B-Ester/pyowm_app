from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .weather_api import weather_at_any_city as ws, all_locations
from .forms import City
import ipdb

def index(request):
    return render(request, 'application_pyowm/index.html')

def city_forecast(request):
    if request.method == 'POST':
        form = City(request.POST)
        if form.is_valid():
            city_name = (str(form.cleaned_data['name_of_city']))
            context = {
                'data': ws(city_name),
                'city': city_name
            }
            return render(request, 'application_pyowm/any_city.html', context)
        else:
            return HttpResponse('Введите корректное назване города')
    else:
        form = City()
        return render(request, 'application_pyowm/any_city.html', {'form': form})
    return HttpResponseRedirect("/city_forecast/")


def barca(request):
    return render(request, 'application_pyowm/barca.html', {'data': ws(all_locations[5])})

def sever(request):
    return render(request, 'application_pyowm/sever.html', {'data': ws(all_locations[0])})

def forecast(request, city):
    return render(request, 'application_pyowm/any_city.html', {'data': ws(str(city))})
