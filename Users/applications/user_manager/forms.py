from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
        
        widgets = {
            'password' : forms.PasswordInput(),
        }
        
        labels = {
            "user" : "Nombre de Usuario",
            "password" : "Contraseña",
        }
        