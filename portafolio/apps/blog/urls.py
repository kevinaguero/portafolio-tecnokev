from django.urls import path
from apps.blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_view, name='blog_view'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]