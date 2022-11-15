from django.urls import path
from . import views

urlpatterns = [
    path('saskia', views.saskia, name='saskia'),
    path('gehitu_saskira/',views.gehitu_saskira,name='gehitu_saskira'),
    path('ezabatu_saskia/',views.ezabatu_saskia,name='ezabatu_saskia'),
    path('saskia_info/<int:id>',views.saskia_info,name='saskia_info'),
    path('erosi', views.erosketa, name='erosketa'),
    path('erosketa/gehitu_bezero_datuak', views.gehitu_bezero_datuak, name='gehitu_bezero_datuak'),
    path('erosketa/erosketaOrdainketa/', views.erosketaOrdainketa, name='erosketaOrdainketa'),
    path('erosketa/erosketaOrdainketa/gehitu_ordainketa_datuak', views.gehitu_ordainketa_datuak, name='gehitu_ordainketa_datuak'),
    path('erosketa/erosketaOrdainketa/erosketarenLaburpena/', views.erosketarenLaburpena, name='erosketarenLaburpena'),
    path('erosketa/erosketaOrdainketa/erosketarenLaburpena/erosketa_bukatu/', views.erosketa_bukatu, name='erosketa_bukatu'),
    path('puntuak_trukatu', views.puntuak_trukatu, name='puntuak_trukatu'),
]
