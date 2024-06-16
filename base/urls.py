from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views 
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogout.as_view(), name="logout")
]