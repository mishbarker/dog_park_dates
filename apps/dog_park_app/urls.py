from django.urls import path, include
from .import views

urlpatterns = [
    path('logout', views.logout), #GET
    path('dashboard', views.dashboard), #GET renders dashboard.html - HOME
    path('remove/<int:id>', views.remove), 
    path('edit/<int:id>', views.edit), #GET renders edit.html
    path('new', views.new), #GET renders to add a new trip
    path('create', views.create), #POST creates (adds to database) a new trip and redirects to show_one/<int:id>
    path('show_one/<int:id>', views.show_one), #GET renders show_one.html
    path('update/<int:id>', views.update), #POST that redirects to /show_one/<int:id>
    path('edit/update/<int:id>', views.update),
]