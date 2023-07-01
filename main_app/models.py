from django.db import models

# Create your models here.

class State(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    parknum = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Territory(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    parknum = models.CharField(max_length=10, default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']