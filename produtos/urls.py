# exibicao/urls.py
from django.urls import path
from .views import exibir_elementos, index, categorias
from . import views
from produtos.views import categorias

app_name = 'produtos'

urlpatterns = [
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<slug:categoria_slug>/', views.produtos_por_categoria, name='produtos_por_categoria'),
    path('', exibir_elementos, name='elementos'),
    path('produto/<slug:produto_slug>/', views.produto_detail, name='produto_detail'),
    path('index', views.index, name='index')
 ]
