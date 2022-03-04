from django.urls import path
from . import views

app_name = 'mysite'

urlpatterns = [
    path('', views.home),
    path('lunch/', views.lunch, name='lunch'),
    path('lotto/', views.lotto, name='lotto'), 
    path('greeting/<str:name>/', views.greeting),
]
