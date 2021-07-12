from rest_framework import viewsets

from tutorial.receitas.models import Receita
from tutorial.receitas.serializers import ReceitaSerializer

class ReceitaViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite que receitas sejam criadas, visualizadas e editadas
    """

    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
