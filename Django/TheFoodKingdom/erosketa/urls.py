from django.urls import path
from . import views

urlpatterns=[
    path('saskia/',views.saskia,name='saskia'),
    path('gehitu_saskira/',views.gehitu_saskira,name='gehitu_saskira'),
    path('ezabatu_saskia/<int:id>',views.ezabatu_saskia,name='ezabatu_saskia'),
]