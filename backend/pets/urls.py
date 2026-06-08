from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pets), 
    path('status/<str:status_pet>/', views.listar_por_status), 
]