from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.get_item_by_id, name="Product_info"),
    path('basket/<int:id>/<int:qty>', views.add_to_basket, name="Add_basket")
]