from django.urls import path
from . import views

urlpatterns=[
    path('saskia/',views.saskia,name='saskia'),
]