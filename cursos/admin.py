from django.contrib import admin

from .models import Avaliacao, Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    lista_display = ('titulo', 'url', 'criacao', 'atualizacoes', 'ativo')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    lista_display = ('curso', 'nome', 'email', 'avaliacao',
                     'criacao', 'atualizacoes', 'ativo')
