from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tutorial.receitas import views

# o DefaultRouter habilita a visualização da API no navegador
# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router = DefaultRouter()
router.register(r'receitas', views.ReceitaViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # url de autenticação para a API no navegador
    # https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#adding-login-to-the-browsable-api
    path('api-auth/', include('rest_framework.urls')),
]
