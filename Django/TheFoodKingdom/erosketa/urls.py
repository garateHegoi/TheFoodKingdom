from django.urls import path
from . import views

urlpatterns = [
    path('saskia/', views.saskia, name='saskia'),
    path('gehitu_saskira/',views.gehitu_saskira,name='gehitu_saskira'),
    path('ezabatu_saskia/',views.ezabatu_saskia,name='ezabatu_saskia'),
    path('saskia_info/<int:id>',views.saskia_info,name='saskia_info'),
    path('erosketa/', views.erosketa, name='erosketa'),
    path('erosketaOrdainketa/', views.erosketaOrdainketa, name='erosketaOrdainketa'),
    path('erosketa/erosketaOrdainketa/', views.erosketaOrdainketa, name='erosketaOrdainketa'),


]
