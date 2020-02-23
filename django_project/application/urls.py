from django.urls import path
#from . import views
#from django.conf.urls import url
from .views import about, age_table, index, information, login, population, privacy, region, register

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('privacy/', privacy, name="privacy"),
    path('about/', about, name="about"),
    path('region/', region, name="region"),
    path('population/', population, name="population"),
    path('age_table/', age_table, name="age_table"),
    path('information/', information, name="information"),
]