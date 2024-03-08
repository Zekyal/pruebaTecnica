from django.db import models

# Create your models here.
class Users(models.Model):
    user = models.CharField('Username', max_length = 20, unique = True, blank = False)
    password = models.CharField('Password', max_length = 20, blank = False)
    
    def __str__(self):
        return f"{self.user}"
    