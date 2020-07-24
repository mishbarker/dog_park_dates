from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.index), #GET renders index.html for landing page
    path('dashboard', views.dashboard), #GET renders dashboard.html - HOME
    path('playdates/new', views.new), #GET renders new.html to add a new playdate and POST to create a new playdate, may add a new park, in database, POST redirects back to dashboard.html
    path('playdates/edit<int:id>', views.new), #GET renders edit.html and POST edits a playdate, may add new park and redirects to dashboard.html
    path('playdates/show_one/<int:id>', views.show_one),


    # path('submit_review/<int:id>', views.submit_review), #POST that redirects to /show_one_review/<int:id>
    # path('delete_review/<int:id>', views.delete_review), #POST/GET redirects to same page /show_one/<int:id>
    # path('user_profile/<int:id>', views.user_profile), #renders profile.html with redirects to /show_one/<int:id> OR HOME OR /new OR /logout
    
]