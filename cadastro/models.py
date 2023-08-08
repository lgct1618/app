from django.db import models
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
import uuid
from datetime import timedelta, datetime

def image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('images/', filename)

class Categoria(models.Model):
    nome = models.CharField(max_length=1000)
    slug_categoria = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.nome

class CadastroDeProdutos(models.Model):
    nome_do_produto = models.CharField(max_length=300, unique=True)
    imagem = models.ImageField(upload_to=image_path)
    categorias = models.ManyToManyField(Categoria)
    descricao = models.CharField(max_length=300)
    preparacao = models.CharField(max_length=10000, blank=True)
    como_conservar = models.CharField(max_length=1000)
    data_de_fabricacao_produto = models.DateField()
    tempo_para_vencimento_produto = models.PositiveIntegerField()  # Número de dias para o vencimento
    data_vencimento_produto = models.DateField(blank=True, null=True)  # Data de vencimento calculada

    slug = models.SlugField(unique=True, default=('formate o nome do produto assim: nome_do_produto'))

    def save(self, *args, **kwargs):
        if not self.slug:  # Verifica se o slug ainda não foi definido
            self.slug = slugify(self.nome_do_produto)

        # Processa a imagem antes de salvar
        if self.imagem:
            img = Image.open(self.imagem)
            img.thumbnail((100, 100))  # Define o tamanho desejado para a imagem (100x100 neste exemplo)

            # Salva a imagem processada em memória
            output = BytesIO()
            format = 'JPEG'  # Define o formato padrão como JPEG

            if img.format == 'PNG':
                format = 'PNG'
            elif img.format == 'GIF':
                format = 'GIF'

            img.save(output, format=format, quality=80)
            output.seek(0)

            # Atualiza o objeto de imagem com a nova imagem processada
            self.imagem = InMemoryUploadedFile(
                output,
                'ImageField',
                f"{self.imagem.name.split('/')[-1].split('.')[0]}.{format.lower()}",
                f'image/{format.lower()}',
                output.tell(),
                None
            )

        # Calcula a data de vencimento apenas se a data de fabricação e a duração do vencimento forem fornecidas
        if self.data_de_fabricacao_produto and self.tempo_para_vencimento_produto:
            self.data_vencimento_produto = self.data_de_fabricacao_produto + timedelta(days=self.tempo_para_vencimento_produto)
        else:
            self.data_vencimento_produto = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_do_produto

class InformacoesNutricionaisEmGramas(models.Model):
    produto = models.OneToOneField(CadastroDeProdutos, on_delete=models.CASCADE, primary_key=True)
    calorias = models.DecimalField(max_digits=5, decimal_places=2)
    carboidratos = models.DecimalField(max_digits=5, decimal_places=2)
    proteinas = models.DecimalField(max_digits=5, decimal_places=2)
    gorduras_totais = models.DecimalField(max_digits=5, decimal_places=2)
    gorduras_saturadas = models.DecimalField(max_digits=5, decimal_places=2)
    gorduras_trans = models.DecimalField(max_digits=5, decimal_places=2)
    fibra_alimentar = models.DecimalField(max_digits=5, decimal_places=2)
    vitamina_a = models.DecimalField(max_digits=5, decimal_places=2)
    vitamina_c = models.DecimalField(max_digits=5, decimal_places=2)
    vitamina_d = models.DecimalField(max_digits=5, decimal_places=2)
    vitamina_e = models.DecimalField(max_digits=5, decimal_places=2)
    vitamina_k = models.DecimalField(max_digits=5, decimal_places=2)
    tiamina = models.DecimalField(max_digits=5, decimal_places=2)
    riboflavina = models.DecimalField(max_digits=5, decimal_places=2)
    niacina = models.DecimalField(max_digits=5, decimal_places=2)
    vitamina_b6 = models.DecimalField(max_digits=5, decimal_places=2)
    vitamina_b12 = models.DecimalField(max_digits=5, decimal_places=2)
    acido_folico = models.DecimalField(max_digits=5, decimal_places=2)
    calcio = models.DecimalField(max_digits=5, decimal_places=2)
    ferro = models.DecimalField(max_digits=5, decimal_places=2)
    magnesio = models.DecimalField(max_digits=5, decimal_places=2)
    fosforo = models.DecimalField(max_digits=5, decimal_places=2)
    potassio = models.DecimalField(max_digits=5, decimal_places=2)
    zinco = models.DecimalField(max_digits=5, decimal_places=2)
    gluten = models.BooleanField()
    leite = models.BooleanField()
    ovos = models.BooleanField()
    peixes = models.BooleanField()
    crustaceos = models.BooleanField()
    amendoim = models.BooleanField()
    frutos_secos = models.BooleanField()
    soja = models.BooleanField()
    trigo = models.BooleanField()
    tamanho_porcao = models.DecimalField(max_digits=5, decimal_places=2)


    etiqueta_para_identificacao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.etiqueta_para_identificacao