from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    carrera = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombres.apellidos
