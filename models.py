from django.db import models

# Create your models here.

class Contact(models.Model):
    User_Name = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Confirm_Password = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    About_Yourself = models.TextField()
