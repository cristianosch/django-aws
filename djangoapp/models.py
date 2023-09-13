from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=150, null=True)
    user = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=400, null=True)
    
    def __str__(self):
        return self.name
