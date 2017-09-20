# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 00:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0004_auto_20170917_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='cep',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message=b'Digite um CEP v\xc3\xa1lido. Ex: 99999-999', regex=b'^\\d{5}-\\d{3}$')], verbose_name=b'CEP'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='endereco',
            field=models.CharField(max_length=200, verbose_name=b'endere\xc3\xa7o'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message=b'Informe um celuar v\xc3\xa1lido. Ex: 99 99999-9999', regex=b'^\\d{2}\\s\\d{5}-\\d{4}$')], verbose_name=b'celular'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone2',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message=b'Informe um telefone v\xc3\xa1lido. Ex: 99 9999-9999', regex=b'^\\d{2}\\s\\d{4}-\\d{4}$')], verbose_name=b'telefone fixo'),
        ),
        migrations.AlterField(
            model_name='equipe',
            name='descricao',
            field=models.TextField(max_length=400, verbose_name=b'descri\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='descricao',
            field=models.TextField(verbose_name=b'descri\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterField(
            model_name='membro',
            name='nome',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message=b'Utilize somente letras, espa\xc3\xa7os e n\xc3\xbameros', regex=b'^(\\w+\\s?)+$')]),
        ),
        migrations.AlterField(
            model_name='quem',
            name='descricao',
            field=models.TextField(verbose_name=b'descri\xc3\xa7\xc3\xa3o'),
        ),
    ]
