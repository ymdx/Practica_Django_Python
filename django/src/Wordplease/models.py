from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):

    ARTE = "ART"
    ESCRITURA = "ESC"
    POLITICA = "POL"
    DEPORTES = "DEP"
    CATEGORIAS = (
        (ARTE, "Arte"),
        (ESCRITURA, "Escritura"),
        (POLITICA, "Politica"),
        (DEPORTES, "Deportes")
    )
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    author = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)  # automáticamente añada la fecha de creación
    modified_at = models.DateTimeField(auto_now=True)  # automáticamente actualiza la fecha al guardar
    categorias = models.CharField(max_length=3, default=ARTE, choices=CATEGORIAS)

    def __str__(self):  # como toString() en Java
        return self.title