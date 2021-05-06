from django.urls import path
from . import views

urlpatterns = [
    ## http://localhost:8000/catalogue
    path('', views.index, name="index"),
    path('<int:id>', views.get_item_by_id, name="Product_info")
]