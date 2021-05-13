from django.urls import path
from . import views

urlpatterns = [
    ## http://localhost:8000/catalogue
    path('', views.orders, name="orders"),
]