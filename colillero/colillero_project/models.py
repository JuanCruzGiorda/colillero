from django.db import models

# Create your models here.

class Colillero(models.Model):
    ip = models.CharField(max_length=50)
    ubicacion = models.TextField(max_length=300)
    ESTADO_CHOICES = [
        ('vacio', 'Vacío'),
        ('porllenarse', 'Porllenarse'),
        ('lleno', 'Lleno'),
    ]
    estado = models.CharField(choices=ESTADO_CHOICES,max_length=20,default='vacio')

    def __str__(self):
        return f"{self.ubicacion} - {self.estado}"

class Colillas(models.Model):
    fecha_Hora = models.DateField()
    cant_colillas = models.IntegerField()
    colillero = models.ForeignKey(Colillero, on_delete=models.CASCADE)
