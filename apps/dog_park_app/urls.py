from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard), #GET renders dashboard.html - HOME
    path('playdates/new', views.new), #GET renders new.html to add a new playdate and POST to create a new playdate, may add a new park, in database, POST redirects back to dashboard.html
    path('playdates/delete/<int:id>', views.delete_playdate),
    path('playdates/<int:id>', views.show_one),
    path('playdates/edit/<int:id>', views.edit_playdate),
<<<<<<< HEAD
=======
    path('playdates/join/<int:playdate_id>', views.join),
    path('playdates/unjoin/<int:playdate_id>', views.un_join),
    path('users/profile', views.profile),
    path('users/create_dog', views.create_dog),
    # path('users/edit_dog', views.edit_dog)
>>>>>>> 22c3781a40935d2ef0276fcc82a3b777c362c92b

    # path('submit_review/<int:id>', views.submit_review), #POST that redirects to /show_one_review/<int:id>
    # path('delete_review/<int:id>', views.delete_review), #POST/GET redirects to same page /show_one/<int:id>
    # path('user_profile/<int:id>', views.user_profile), #renders profile.html with redirects to /show_one/<int:id> OR HOME OR /new OR /logout
<<<<<<< HEAD
    
=======
>>>>>>> 22c3781a40935d2ef0276fcc82a3b777c362c92b
]