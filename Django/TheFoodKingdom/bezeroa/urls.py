from django.urls import path
from . import views

urlpatterns=[
    path('',views.profila,name='profila'),
    path('profilaaldatu/',views.profilaaldatu,name='profilaaldatu'),
]