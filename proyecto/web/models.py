from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

#entidad que se va a ralacionar con auto



class Auto(models.Model):
    marca = models.CharField(default="generico",max_length=200)
    modelo = models.CharField(default="generico",max_length=200)
    cilindrada = models.CharField(default="Sin Especificar",max_length=200)
    imagen = models.ImageField(upload_to="Autos", default='giphy.webp')
    
    anno = models.CharField(max_length=200)
    precio = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    

    def __str__(self):
        return self.marca
class ImagenAuto(models.Model):
    imagen = models.ImageField(upload_to="Autos")
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name="imagenes", default='giphy.webp')

    
opciones_generos = [
    [0, "Hombre"],
    [1, "Mujer"],
    [2, "Otro"]
]
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    appaterno = models.CharField(max_length=200)
    apmaterno = models.CharField(max_length=200)
    run = models.CharField(max_length=200)
    celular = models.IntegerField(validators=[MinValueValidator(0)])
    email = models.EmailField()
    fecha_nac = models.DateField()
    genero = models.IntegerField(choices=opciones_generos)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    
    imagen = models.ImageField(upload_to="Productos",default='enProceso.png', null=True)
    marca = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField(validators=[MinValueValidator(0)])
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

