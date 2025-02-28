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