from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from tutorial.receitas.models import Receita
from tutorial.receitas.serializers import ReceitasSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite que users sejam criados e editados.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ReceitaViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite que receitas sejam criadas e editadas.
    """
    queryset = Receita.objects.all()
    serializer_class = ReceitasSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
