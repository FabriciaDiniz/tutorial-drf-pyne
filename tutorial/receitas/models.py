from django.db import models
from django.contrib.auth.models import User

class Receita(models.Model):
    nome = models.CharField(max_length=50, default="")
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    # Model User padrão do Django
    # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#user-model
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nome
