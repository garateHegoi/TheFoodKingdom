from django.urls import path
from . import views

urlpatterns=[
    path('',views.profila,name='profila'),
    path('profila/profilaaldatu/',views.profilaaldatu,name='profilaaldatu'),
]