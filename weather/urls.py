
from django.conf.urls import url
from django.contrib import admin
from application_pyowm import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^city_forecast/', views.city_forecast, name='city_forecast'),
    url(r'^sever/', views.sever, name='sever'),
    url(r'^barca/', views.barca, name='barca'),
    url(r'^forecast/(?P<city>[\w])', views.forecast, name='forecast')
]


