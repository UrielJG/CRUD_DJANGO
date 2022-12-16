from django.db import models

# Create your models here.
class persona(models.Model):
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=200)