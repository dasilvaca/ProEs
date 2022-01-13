from django.db import models

# Create your models here.

class Carros(models.Model):
    modelo = models.IntegerField(default=0)
    marca = models.CharField(default="N/A", max_length=128)
    placa = models.CharField(default="Sin Registro", max_length=128, primary_key=True)

    def __str__(self):
        return str(self.placa)

class Consecionario(models.Model):
    carros = models.ForeignKey(Carros, on_delete=models.CASCADE)