from django.urls import path
from . import views

urlpatterns=[
    path('',views.profila,name='profila'),
    path('profilaaldatu/<int:id_erabiltzaile>',views.profilaaldatu,name='profilaaldatu'),
    path('erregistratu/',views.erregistratu,name='erregistratu'),
]