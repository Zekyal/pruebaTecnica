from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Models
from .models import Users
# Forms
from .forms import UserForm

# Create your views here.
class ListAllUsers(ListView):
    template_name = "home.html"
    model = Users
    context_object_name = "users"
    
class NewUser(CreateView):
    template_name = "new-user.html"
    model = Users
    form_class = UserForm
    success_url = '/home/'
    
class EditUser(UpdateView):
    template_name = "new-user.html"
    model = Users
    form_class = UserForm
    success_url = '/home/'
    
class DeleteUser(DeleteView):
    template_name = "delete-user.html"
    model = Users
    success_url = '/home/'