from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .weather_api import weather_at_any_city, all_locations, time_now
from .forms import City

def index(request):
    return render(request, 'application_pyowm/index.html')

def city_forecast(request):
    if request.method == 'POST':
        form = City(request.POST)
        if form.is_valid():
            city_name = (str(form.cleaned_data['name_of_city']))
            return render(request, 'application_pyowm/any_city.html', {'data': weather_at_any_city(city_name)})
        else:
            return HttpResponse('Введите корректное назване города')
    else:
        form = City()
        return render(request, 'application_pyowm/any_city.html', {'form': form})
    return HttpResponseRedirect("/city_forecast/")


def barca(request):
    return render(request, 'application_pyowm/barca.html', {'data': weather_at_any_city(all_locations[5])})

def sever(request):
    return render(request, 'application_pyowm/sever.html', {'data' : weather_at_any_city(all_locations[0])})
