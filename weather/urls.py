from django.conf.urls import url
from django.contrib import admin
from application_pyowm import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^city_forecast/', views.city_forecast, name='city_forecast'),
    url(r'^forecast/(?P<city>[\w])', views.forecast, name='forecast'),
    url(r'^future_fc', views.future_fc, name='future_fc'),
    url(r'^coords/', views.coords, name='coords'),
    url(r'^sever/', views.sever, name='sever'),
    url(r'^lvov/', views.lvov, name='lvov'),
    url(r'^kharkov/', views.kharkov, name='kharkov'),
    url(r'^odessa/', views.odessa, name='odessa'),
    url(r'^kiev/', views.kiev, name='kiev'),
    url(r'^dnepr/', views.dnepr, name='dnepr'),
    url(r'^barca/', views.barca, name='barca'),
    url(r'^madrid/', views.madrid, name='madrid'),
    url(r'^paris/', views.paris, name='paris'),
    url(r'^berlin/', views.berlin, name='berlin'),
    url(r'^london/', views.london, name='london'),
    url(r'^lissabon/', views.lissabon, name='lissabon'),
]


