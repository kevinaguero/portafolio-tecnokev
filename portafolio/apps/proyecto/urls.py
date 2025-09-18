from django.urls import path
from apps.proyecto import views

app_name = 'proyecto'
urlpatterns = [
    path('', views.proyecto_view, name='proyecto_view'),
]