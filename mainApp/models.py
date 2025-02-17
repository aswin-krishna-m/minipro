from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=150,unique=True)
    email = models.EmailField(max_length=254,unique=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username