from django.urls import path
from .views import ListAllUsers, NewUser, EditUser, DeleteUser

# Urls de la pagina Web
urlpatterns = [
    path('home/', ListAllUsers.as_view()),
    path('home/new-user', NewUser.as_view()),
    path('home/<int:pk>/edit-user', EditUser.as_view(), name = "Edit"),
    path('home/<int:pk>/delete-user', DeleteUser.as_view(), name = "Delete"),
]
