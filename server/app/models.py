from django.db import models

# Create your models here.

class userdata(models.Model):
    Name= models.CharField(max_length=100)
    Gender= models.CharField(max_length=100)
    Password= models.CharField(max_length=100)
    Contact= models.IntegerField()
    Email = models.EmailField()
    class Meta:
        db_table = "userdata"

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(unique=True)
    sec = models.CharField(max_length=10)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    guardian_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
