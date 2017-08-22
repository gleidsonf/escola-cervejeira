# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-21 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170821_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]