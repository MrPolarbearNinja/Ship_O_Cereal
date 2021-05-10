from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    ## http://localhost:8000/catalogue
    path('', views.index, name="index"),
    path('create-account', views.create_account, name='create_account'),
    path('edit-account', views.edit_account, name='edit_account'),
    path('login', LoginView.as_view(template_name='account_log_in/acount_login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'), #FIXME
    # path('signup', views.create_account, name='create_account')
]