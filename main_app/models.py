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

class Place(models.Model):

    name = models.CharField(max_length=150)
    placetype = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="places")

    def __str__(self):
        return self.name