from django.contrib.auth.models import User
from rest_framework import serializers

from tutorial.receitas.models import Receita

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # o HyperlinkedModelSerializer adiciona o campo url ao modelo, utilizando ele como chave primária
    # https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer
    class Meta:
        model = User
        fields = ['username', 'email', 'url', 'receitas']


class ReceitasSerializer(serializers.ModelSerializer):
    # O source controla que atributo é usado para popular o campo
    # pode apontar para qualquer atributo da instancia serializada
    autor = serializers.ReadOnlyField(source='autor.username')

    class Meta:
        model = Receita
        fields = ['nome', 'ingredientes', 'modo_preparo', 'autor']

    # validade_<nome_do_campo> cria uma validação customizada para campos específicos
    # https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
    def validate_modo_preparo(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Modo de preparo deve ter no mínimo 10 caracteres")

        return value
