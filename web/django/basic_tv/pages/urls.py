from importlib.resources import path
from django.urls import path
from . import views

app_name ='pages'

urlpatterns = [
    path('dinner/<str:menu>/<str:count>/', views.dinner),
    path('check/', views.check),
]