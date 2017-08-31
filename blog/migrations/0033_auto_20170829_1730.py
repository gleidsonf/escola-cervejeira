# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-29 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20170828_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='cep',
        ),
        migrations.AlterField(
            model_name='curso',
            name='email',
            field=models.EmailField(default='contato@escolacervejeira.com.br', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]