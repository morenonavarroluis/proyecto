from django.db import models

# Create your models here.

class Empleado(models.Model):
    id = models.AutoField(primary_key=True) 
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_contratacion = models.CharField(max_length=10)  # Assuming date is stored as a string
    cargo = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='imagenes/', null=True , verbose_name='Foto del empleado')
    
    def __str__(self):
        fila = "nombre :" + self.nombre + " apellido: " + self.apellido + " cargo: " + self.cargo
        return fila
    
    def delete(self, using=None , keep_parents=False):
        self.foto.storage.delete(self.foto.name)
        super().delete()