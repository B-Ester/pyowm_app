from django import forms

class City(forms.Form):
    name_of_city = forms.CharField(label='Введите город', max_length=50)

class Cords(forms.Form):
    long = forms.FloatField(label='Широта', max_value=90, min_value=-90)
    lat = forms.FloatField(label='Долгота', max_value=180, min_value=-180)