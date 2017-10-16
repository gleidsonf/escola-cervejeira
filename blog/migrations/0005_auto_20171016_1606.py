# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 18:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170929_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerveja',
            name='data_de_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='data de criação'),
        ),
        migrations.AlterField(
            model_name='cerveja',
            name='data_de_publicacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data de publicação'),
        ),
        migrations.AlterField(
            model_name='cerveja',
            name='descricao',
            field=models.TextField(max_length=1000, verbose_name='avaliação da cerveja'),
        ),
        migrations.AlterField(
            model_name='cerveja',
            name='nota1',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='aparência'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='cep',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Digite um CEP válido. Ex: 99999-999', regex='^\\d{5}-\\d{3}$')], verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='data_de_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='data de criação'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='data_de_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='data de início'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='data_de_publicacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data de publicação'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descricao',
            field=models.TextField(verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='duracao',
            field=models.CharField(max_length=100, verbose_name='duração'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='endereco',
            field=models.CharField(max_length=200, verbose_name='endereço'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Utilize somente letras, espaços e números', regex='^(\\w+\\s?)+$')]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='organizador',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Utilize somente letras, espaços e números', regex='^(\\w+\\s?)+$')]),
        ),
        migrations.AlterField(
            model_name='curso',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='preço'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='telefone',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message='Informe um telefone válido. Ex: 99 99999-9999', regex='^\\d{2}\\s\\d{5}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='evento',
            name='descricao',
            field=models.TextField(verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='organizador',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Utilize somente letras, espaços e números', regex='^(\\w+\\s?)+$')]),
        ),
        migrations.AlterField(
            model_name='evento',
            name='telefone',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message='Informe um telefone válido. Ex: 99 99999-9999', regex='^\\d{2}\\s\\d{5}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_de_publicacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='data de publicação'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_de_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='data de criação'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.BooleanField(default=False, verbose_name='é um evento?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='título'),
        ),
    ]