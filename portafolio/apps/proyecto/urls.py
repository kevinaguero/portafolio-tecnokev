from django.urls import path
from apps.proyecto import views

app_name = 'proyecto'
urlpatterns = [
    path('', views.proyectos_view, name='proyectos_view'),
]