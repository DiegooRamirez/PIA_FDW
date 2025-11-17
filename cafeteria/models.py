from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    imagen_url = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.precio}\n\t{self.descripcion}"
    
class Opinion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del cliente")
    comentario = models.TextField(verbose_name="Comentario")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")

    def __str__(self):
        return f"{self.nombre}\n{self.comentario}\n\t\t\t{self.fecha.strftime('%d/%m/%Y')}"
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.asunto} - {self.nombre}"

class Auto(models.Model):
    marca = models.CharField(max_length=50)              
    modelo = models.CharField(max_length=50)             
    año = models.PositiveIntegerField()                  
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    calle = models.CharField(max_length=200)
    colonia = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    codigoPostal = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}\n{self.calle}, {self.colonia}\n{self.ciudad}\n{self.codigoPostal}"
