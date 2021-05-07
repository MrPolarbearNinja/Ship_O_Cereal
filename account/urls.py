from django.urls import path
from . import views

urlpatterns = [
    ## http://localhost:8000/catalogue
    path('', views.index, name="index"),
    path('create_account', views.create_account, name='create_account'),
]