# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170918_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceiro',
            name='nome',
            field=models.CharField(max_length=70),
        ),
    ]
