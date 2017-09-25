# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 13:43
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cerveja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estilo', models.CharField(max_length=100, verbose_name=b'estilo')),
                ('categoria', models.CharField(max_length=100)),
                ('nota1', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name=b'apar\xc3\xaancia')),
                ('nota2', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name=b'aroma')),
                ('nota3', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name=b'sabor e corpo')),
                ('nota4', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name=b'paladar')),
                ('imagem', models.ImageField(upload_to=b'cervejas/')),
                ('descricao', models.TextField(max_length=1000, verbose_name=b'avalia\xc3\xa7\xc3\xa3o da cerveja')),
                ('data_de_criacao', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name=b'data de cria\xc3\xa7\xc3\xa3o')),
                ('data_de_publicacao', models.DateTimeField(blank=True, null=True, verbose_name=b'data de publica\xc3\xa7\xc3\xa3o')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message=b'Utilize somente letras, espa\xc3\xa7os e n\xc3\xbameros', regex=b'^(\\w+\\s?)+$')], verbose_name=b'nome do cliente')),
                ('imagem', models.ImageField(upload_to=b'clientes/', verbose_name=b'logo do cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message=b'Utilize somente letras, espa\xc3\xa7os e n\xc3\xbameros', regex=b'^(\\w+\\s?)+$')])),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name=b'pre\xc3\xa7o')),
                ('local', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200, verbose_name=b'endere\xc3\xa7o')),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message=b'Digite um CEP v\xc3\xa1lido. Ex: 99999-999', regex=b'^\\d{5}-\\d{3}$')], verbose_name=b'CEP')),
                ('cidade', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to=b'cursos/')),
                ('descricao', models.TextField(verbose_name=b'descri\xc3\xa7\xc3\xa3o')),
                ('organizador', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message=b'Utilize somente letras, espa\xc3\xa7os e n\xc3\xbameros', regex=b'^(\\w+\\s?)+$')])),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('telefone', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message=b'Informe um telefone v\xc3\xa1lido. Ex: 99 99999-9999', regex=b'^\\d{2}\\s\\d{5}-\\d{4}$')])),
                ('data_de_inicio', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'data de in\xc3\xadcio')),
                ('duracao', models.CharField(max_length=100, verbose_name=b'dura\xc3\xa7\xc3\xa3o')),
                ('data_de_criacao', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name=b'data de cria\xc3\xa7\xc3\xa3o')),
                ('data_de_publicacao', models.DateTimeField(blank=True, null=True, verbose_name=b'data de publica\xc3\xa7\xc3\xa3o')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=b'Eventos', editable=False, max_length=10, unique=True)),
                ('imagem', models.ImageField(upload_to=b'eventos/')),
                ('descricao', models.TextField(verbose_name=b'descri\xc3\xa7\xc3\xa3o')),
                ('organizador', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message=b'Utilize somente letras, espa\xc3\xa7os e n\xc3\xbameros', regex=b'^(\\w+\\s?)+$')])),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('telefone', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message=b'Informe um telefone v\xc3\xa1lido. Ex: 99 99999-9999', regex=b'^\\d{2}\\s\\d{5}-\\d{4}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('endereco', models.CharField(max_length=100, null=True)),
                ('position', geoposition.fields.GeopositionField(default=b'-3.75572,-38.517394', max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name=b't\xc3\xadtulo')),
                ('tag', models.BooleanField(default=False, verbose_name=b'\xc3\xa9 um evento?')),
                ('imagem', models.ImageField(upload_to=b'posts/')),
                ('texto', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date_de_criacao', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name=b'data de cria\xc3\xa7\xc3\xa3o')),
                ('data_de_publicacao', models.DateTimeField(blank=True, null=True, verbose_name=b'data de publica\xc3\xa7\xc3\xa3o')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
