from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('karta/',views.karta,name='karta'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('karta_sailkatua/',views.karta_sailkatua,name='karta_sailkatua'),
    path('kokapena/',views.kokapena,name='kokapena'),
    path('erregistroa/',views.erregistroa,name='erregistroa'),
    path('profila<int:id>/',views.profila,name='profila'),
    path('saskia/',views.saskia,name='saskia'),
    path('produktua/<int:id>',views.produktua,name='produktua'),
    ]