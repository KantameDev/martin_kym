
from django.urls import path
from . import views

urlpatterns=[
    path('inscription',views.inscriptionPage, name='inscription'),
    path('accès',views.accesPage, name='acces'),
    path('quitter',views.logoutUser, name='quitter'),
]
