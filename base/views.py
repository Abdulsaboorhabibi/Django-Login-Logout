from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class IndexView(TemplateView):
    template_name = "base/index.html"

class UserLoginView(LoginView):
    template_name = "base/login.html"
    feilds = "__all__"
    success_url = reverse_lazy("/")
    redirect_authenticated_user = True

class UserLogout(LogoutView):
    next_page = "/"
