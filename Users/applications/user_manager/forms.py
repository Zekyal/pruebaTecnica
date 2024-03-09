from django import forms
from .models import Users

# Creacion de formularios para crear/actualizar un registro.
class UserForm(forms.ModelForm):
    class Meta:
        # Declaracion del Modelo a usar para el formulario
        model = Users
        # Campos para el formulario. Se usaran todos los campos del Modelo
        fields = '__all__'
        
        # Configuraciones adicionales
        widgets = {
            'password' : forms.PasswordInput(),
        }
        
        # Cambiar el nombre que se mostrara para el formulario
        labels = {
            "user" : "Nombre de Usuario",
            "password" : "Contraseña",
        }