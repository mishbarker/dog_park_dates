from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard), #GET renders dashboard.html - HOME
    path('playdates/new', views.new), #GET renders new.html to add a new playdate and POST to create a new playdate, may add a new park, in database, POST redirects back to dashboard.html
    path('playdates/delete/<int:id>', views.delete_playdate),
    path('playdates/<int:id>', views.show_one),
    path('playdates/edit/<int:id>', views.edit_playdate),
]