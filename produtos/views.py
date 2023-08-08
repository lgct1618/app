# exibicao/views.py
from django.shortcuts import render, get_object_or_404
from cadastro.models import CadastroDeProdutos, Categoria

def exibir_elementos(request):
    elementos = CadastroDeProdutos.objects.all()
    return render(request, 'index.html', {'elementos': elementos})

def index(request):
    return render(request, 'index.html')

def produto_detail(request, produto_slug):
    produto = get_object_or_404(CadastroDeProdutos, slug=produto_slug)
    return render(request, 'produto_detail.html', {'produto': produto})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

def produtos_por_categoria(request, categoria_slug):
    categoria = get_object_or_404(Categoria, slug_categoria=categoria_slug)
    produtos = CadastroDeProdutos.objects.filter(categorias=categoria)
    return render(request, 'produtos_por_categoria.html', {'categoria': categoria, 'produtos': produtos})