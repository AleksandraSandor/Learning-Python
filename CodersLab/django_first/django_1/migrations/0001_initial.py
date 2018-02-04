# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 12:45
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
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('available', models.BooleanField(default=True)),
                ('available_from', models.DateField(null=True)),
            ],
        ),
    ]