from django.urls import path
from .views import UserLoginView, Profile
from django.contrib.auth.views import LogoutView

app_name = "users"

urlpatterns = [
    path(
        "",
        UserLoginView.as_view(), 
        name='user_login'
    ),
    path(
        'profile/',
        Profile,
        name='user_profile'
    ),
    path(
        'logout/',
        LogoutView.as_view(next_page="users:user_login"),
        name='user_logout'
    ),
]