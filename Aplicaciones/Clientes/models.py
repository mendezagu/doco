from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=20)
    documento = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    parentesco = models.CharField(max_length=100)
    menorNombre = models.CharField(max_length=100)
    menorApellido = models.CharField(max_length=100)
    fecha_nacimientoMenor = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"