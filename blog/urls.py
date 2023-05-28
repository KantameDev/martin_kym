from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('formation_LaTeX', views.flatex, name='flatex'),
    path('formation_geogebra', views.fgeogeb, name='fgeogeb'),
]
