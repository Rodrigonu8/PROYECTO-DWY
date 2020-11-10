from django.db import models

# Create your models here.

class Bicicleta(models.Model):
    id_bicicleta = models.IntegerField(primary_key=True)
    modelo = models.CharField(max_length=50)
    candado = models.BooleanField(default=False)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.id_bicicleta


class Portico(models.Model):
    id_portico = models.IntegerField()
    id_bicicleta = models.ForeignKey(Bicicleta,null=False, on_delete=models.CASCADE)
    ubicacion = models.TextField()

    def __str__(self):
        return self.id_bicicleta


