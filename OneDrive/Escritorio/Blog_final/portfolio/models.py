from django.db import models
from django.db.models.fields import CharField, URLField, TextField
from django.db.models.fields.files import ImageField



class Project(models.Model):
    Titulo = CharField(max_length=100)
    Descripcion = TextField(max_length=2500)
    Imagen = ImageField(upload_to='portfolio/images/')
    URL = URLField(blank=True) 

    def __str__(self):
        return self.Titulo
