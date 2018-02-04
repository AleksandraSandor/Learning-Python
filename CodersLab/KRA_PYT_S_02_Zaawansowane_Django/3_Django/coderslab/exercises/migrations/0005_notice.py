# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-16 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_auto_20171116_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('add_student_notice', 'Testowe uprawnienie'),),
            },
        ),
    ]