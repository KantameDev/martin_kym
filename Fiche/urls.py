from django.urls import path
from .views import telecharge_fiche
from .import views


urlpatterns=[
    path('fiches/<int:fiche_id>/', telecharge_fiche,name='telecharge_fiche'),
    path('fiches',views.Fich, name='fiches'),
]