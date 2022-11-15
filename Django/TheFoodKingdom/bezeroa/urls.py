from django.urls import path
from . import views

urlpatterns=[
    path('profila/',views.profila,name='profila'),
    path('profilaaldatu/<int:id_erabiltzaile>/',views.profilaaldatu,name='profilaaldatu'),
    path('profilaaldatudb/<int:id>',views.profilaaldatudb,name='profilaaldatudb'),
    path('erregistratu/',views.erregistratu,name='erregistratu'),
    path('erregistroa/',views.erregistroa,name='erregistroa'),
]