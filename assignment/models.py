from django.db import models

# Create your models here.
class Login(models.Model):
    email_id= models.EmailField()
    password = models.CharField(max_length=20)