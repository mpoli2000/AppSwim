from django.db import models

# Create your models here.
class Nadador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField(default=18)

    def __str__(self):
        return f'nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Edad: {self.edad}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}'

class Estilo(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return f'nombre: {self.nombre} - descripcion: {self.descripcion}'

class Slot(models.Model):
    fecha = models.DateField()
    horario = models.TimeField()
    duracion = models.IntegerField(default=45)

    def __str__(self):
        return f'fecha: {self.fecha} - horario: {self.horario} - duaracion: {self.duracion}'
