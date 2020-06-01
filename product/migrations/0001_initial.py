# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-06 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=20)),
                ('barcode', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(max_length=255, null=True, upload_to='media')),
                ('price', models.IntegerField(default=0)),
                ('manufactured_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('description', models.TextField()),
                ('section', models.CharField(max_length=5)),
            ],
        ),
    ]
