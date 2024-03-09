from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Models
from .models import Users
# Forms
from .forms import UserForm

# Vista Read
# Lista a todos los usuarios
class ListAllUsers(ListView):
    template_name = "home.html"
    model = Users
    context_object_name = "users"
        

# Vista Create
# Insertar nuevos usuarios 
class NewUser(CreateView):
    template_name = "new-user.html"
    model = Users
    form_class = UserForm
    success_url = '/home/'


# Vista Update
# Actualizar usuario existente    
class EditUser(UpdateView):
    template_name = "new-user.html"
    model = Users
    form_class = UserForm
    success_url = '/home/'


# Vista Delete
# Eliminar usuario existente       
class DeleteUser(DeleteView):
    template_name = "delete-user.html"
    model = Users
    success_url = '/home/'