# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170820_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to=b''),
        ),
    ]
