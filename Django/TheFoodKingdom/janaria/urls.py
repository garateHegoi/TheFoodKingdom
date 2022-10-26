from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('karta/',views.karta,name='karta'),
    path('kokapena/',views.kokapena,name='kokapena'),
    path('erregistroa/',views.erregistroa,name='erregistroa'),
    path('profila/',views.profila,name='profila'),
    path('saskia/',views.saskia,name='saskia'),
    ]