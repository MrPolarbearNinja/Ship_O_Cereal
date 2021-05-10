from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    ## http://localhost:8000/catalogue
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('create_account', views.create_account, name='create_account'),
    path('profile', views.Profile, name='profile'),
    path('login', LoginView.as_view(template_name='account_log_in/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
]