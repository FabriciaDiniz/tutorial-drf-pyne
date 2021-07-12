from rest_framework import serializers
from tutorial.receitas.models import Receita

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
