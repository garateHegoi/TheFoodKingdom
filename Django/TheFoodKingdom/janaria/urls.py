from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('karta/',views.karta,name='karta'),
    path('karta/index/',views.index_bueltatu,name='index_bueltatu'),
    path('kokapena/',views.kokapena,name='kokapena'),
    ]