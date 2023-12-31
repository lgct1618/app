# Generated by Django 4.2.4 on 2023-08-28 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacoesNutricionaisEmGramas',
            fields=[
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cadastro.cadastrodeprodutos')),
                ('calorias', models.DecimalField(decimal_places=2, max_digits=5)),
                ('carboidratos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('proteinas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gorduras_totais', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gorduras_saturadas', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gorduras_trans', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fibra_alimentar', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamina_a', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamina_c', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamina_d', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamina_e', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamina_k', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tiamina', models.DecimalField(decimal_places=2, max_digits=5)),
                ('riboflavina', models.DecimalField(decimal_places=2, max_digits=5)),
                ('niacina', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamina_b6', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vitamina_b12', models.DecimalField(decimal_places=2, max_digits=5)),
                ('acido_folico', models.DecimalField(decimal_places=2, max_digits=5)),
                ('calcio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ferro', models.DecimalField(decimal_places=2, max_digits=5)),
                ('magnesio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fosforo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('potassio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('zinco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('gluten', models.BooleanField()),
                ('leite', models.BooleanField()),
                ('ovos', models.BooleanField()),
                ('peixes', models.BooleanField()),
                ('crustaceos', models.BooleanField()),
                ('amendoim', models.BooleanField()),
                ('frutos_secos', models.BooleanField()),
                ('soja', models.BooleanField()),
                ('trigo', models.BooleanField()),
                ('tamanho_porcao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('etiqueta_para_identificacao', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='slug_categoria',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nome',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='InformacoesNutricionais',
        ),
    ]
