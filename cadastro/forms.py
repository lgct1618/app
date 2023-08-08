from django import forms
from .models import CadastroDeProdutos, Categoria, InformacoesNutricionaisEmGramas


class ProdutoForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = CadastroDeProdutos
        fields = ['nome_do_produto', 'imagem', 'descricao', 'preparacao', 'como_conservar', 'categorias', 'data_de_fabricacao_produto', 'tempo_para_vencimento_produto']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'slug']

class InformacoesNutricionaisForm(forms.ModelForm):
    class Meta:
        model = InformacoesNutricionaisEmGramas
        fields = '__all__'