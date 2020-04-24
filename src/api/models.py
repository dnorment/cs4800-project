# Create your models here.
from django.db import models

class Bot(models.Model):
    
    name = models.CharField(max_length=60)
    #alias = models.CharField(max_length=60)
    userId = models.UUIDField
    
    
    def __str__(self):
        return self.name
#end Bot

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name
#end Hero