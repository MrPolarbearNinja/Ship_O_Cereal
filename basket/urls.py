from django.urls import path
from . import views

urlpatterns = [
    ## http://localhost:8000/catalogue
    path('', views.basket, name="basket"),
    path('delete_from_basket/<int:id>', views.delete_from_basket, name="delete_from_basket"),
]