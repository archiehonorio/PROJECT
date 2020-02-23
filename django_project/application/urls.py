from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('privacy/',views.privacy,name='privacy'),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('region/',views.region,name='region'),
    path('population/',views.population,name='population'),
    path('age_table/',views.age_table,name='age_table'),
    path('information/',views.information,name='information'),
]