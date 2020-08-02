from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard), #GET renders dashboard.html - HOME
    path('playdates/new', views.new), #GET renders new.html to add a new playdate and POST to create a new playdate, may add a new park, in database, POST redirects back to dashboard.html
    path('playdates/delete/<int:id>', views.delete_playdate),
    path('playdates/<int:id>', views.show_one),
    path('playdates/<int:playdate_id>/edit', views.edit_playdate),
    path('playdates/join/<int:playdate_id>', views.join),
    path('playdates/unjoin/<int:playdate_id>', views.un_join),
    path('users/profile', views.profile),
    path('users/create_dog', views.create_dog),
    path('users/<int:dog_id>/delete', views.delete_dog),
    path('users/<int:dog_id>/edit', views.edit_dog),
    path('users/edit_user', views.edit_user),
]