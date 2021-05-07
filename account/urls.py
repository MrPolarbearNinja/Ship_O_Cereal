from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create_account', views.create_account, name='create_account'),
    path('edit_account', views.edit_account, name='edit_account'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='Login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout')
]