from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('playdates/new', views.new),
    path('playdates/edit/<int:playdate_id>', views.edit_playdate),
    path('playdates/delete/<int:id>', views.delete_playdate),
    path('playdates/<int:id>', views.show_one),
<<<<<<< HEAD
    path('playdates/edit/<int:id>', views.edit_playdate),
=======
    path('playdates/<int:playdate_id>/edit', views.edit_playdate),
>>>>>>> 73aa4373a7a95ce7237f08839f445f6fa6f9053b
    path('playdates/join/<int:playdate_id>', views.join),
    path('playdates/unjoin/<int:playdate_id>', views.un_join),
    path('users/profile', views.profile),
    path('users/create_dog', views.create_dog),
<<<<<<< HEAD
    # path('users/edit_dog', views.edit_dog)

    # path('submit_review/<int:id>', views.submit_review), #POST that redirects to /show_one_review/<int:id>
    # path('delete_review/<int:id>', views.delete_review), #POST/GET redirects to same page /show_one/<int:id>
    # path('user_profile/<int:id>', views.user_profile), #renders profile.html with redirects to /show_one/<int:id> OR HOME OR /new OR /logout
=======
    path('users/<int:dog_id>/delete', views.delete_dog),
    path('users/<int:dog_id>/edit', views.edit_dog),
    path('users/edit_user', views.edit_user),

>>>>>>> 73aa4373a7a95ce7237f08839f445f6fa6f9053b
]