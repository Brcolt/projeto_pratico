from django.db import models

# Create your models here.


class Livro(models.Model):
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    isbn = models.IntegerField()
    numero_paginas = models.IntegerField()
    titulo = models.CharField(max_length=50)
    ano_publicacao = models.IntegerField()
    email_editora = models.EmailField()