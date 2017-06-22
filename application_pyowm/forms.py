from django import forms

class City(forms.Form):
    name_of_city = forms.CharField(label='Введите город', max_length=50)