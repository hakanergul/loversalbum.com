from django.urls import path
from . import views

urlpatterns = [
    path('', views.ilan_detay, name='ilan'), 
    path('<int:ilan_id>/', views.ilan_detay, name = 'ilandetaylari'),
]
