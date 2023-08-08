from django.contrib import admin

from .models import CadastroDeProdutos, Categoria, InformacoesNutricionaisEmGramas

admin.site.register(CadastroDeProdutos)
admin.site.register(Categoria)
admin.site.register(InformacoesNutricionaisEmGramas)

class InformacoesNutricionaisEmGramasInline(admin.StackedInline):
    model = InformacoesNutricionaisEmGramas

class CadastroDeProdutosAdmin(admin.ModelAdmin):
    inlines = [InformacoesNutricionaisEmGramasInline]
