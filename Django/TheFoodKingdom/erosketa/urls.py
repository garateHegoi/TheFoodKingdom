from django.urls import path
from . import views

urlpatterns = [
    path('saskia/', views.saskia, name='saskia'),
    path('erosketa/', views.erosketa, name='erosketa'),
    path('erosketaOrd/', views.erosketaOrd, name='erosketaOrd'),
]
