from django.db import models

# Creacion del Modelo de Usuarios
# Django crea la Base de Datos en SQLite a partir de este Modelo
class Users(models.Model):
    user = models.CharField('Username', max_length = 20, unique = True, blank = False)
    password = models.CharField('Password', max_length = 20, blank = False)
    
    def __str__(self):
        return f"{self.user}"
    