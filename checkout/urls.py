from django.urls import path
from . import views

urlpatterns = [
    ## http://localhost:8000/catalogue
    path('', views.index2, name="index"),
    path('review', views.make_purchase, name="review")
]