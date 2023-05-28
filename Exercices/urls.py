from django.urls import path
from .views import telecharge_fichier,download_pdf,tele_fichier,telecharge_correct
from .import views


urlpatterns=[
    path('fichier/<int:exercice_id>/', telecharge_fichier,name='telecharge_fichier'),
    path('coorect/<int:exercice_id>/', telecharge_correct,name='telecharge_correct'),
    path('exercice',views.Exo, name='exercice'),
    path('pdf/<int:exercice_id>/', tele_fichier,name='tele_fichier'),
]