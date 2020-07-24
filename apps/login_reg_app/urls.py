from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin),
    path('register', views.register),
    path('logout', views.logout)
]