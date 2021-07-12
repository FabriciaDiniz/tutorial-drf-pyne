from django.db import models

# Create your models here.

class Receita(models.Model):
    nome = models.CharField(max_length=50, default="")
    ingredientes = models.TextField()
    modo_preparo = models.TextField()

    def __str__(self):
        return self.nome
