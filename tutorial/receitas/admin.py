from django.contrib import admin

from tutorial.receitas.models import Receita


class ReceitasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Receita, ReceitasAdmin)
