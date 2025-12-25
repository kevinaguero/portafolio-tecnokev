from django.urls import path
from minijuegos import views

app_name = 'minijuegos'
urlpatterns = [
    path('', views.minijuegos_view, name='minijuegos_view'),
]
