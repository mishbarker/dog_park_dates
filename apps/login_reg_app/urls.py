from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index), #GET renders index.html for register or login
    path('register', views.register), #POST redirect to index or redirect to /dashboard
    path('login', views.login), #POST redirect to index or redirect to /dashboard
]