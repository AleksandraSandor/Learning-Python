# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_auto_20170315_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGrades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField(choices=[(1, '1'), (1.5, '1+'), (1.75, '2-'), (2, '2'), (2.5, '2+'), (2.75, '3-'), (3, '3'), (3.5, '3+'), (3.75, '4-'), (4, '4'), (4.5, '4+'), (4.75, '5-'), (5, '5'), (5.5, '5+'), (5.75, '6-'), (6, '6')])),
                ('school_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.SchoolSubject')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='grades',
            field=models.ManyToManyField(through='exercises.StudentGrades', to='exercises.SchoolSubject'),
        ),
        migrations.AddField(
            model_name='studentgrades',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Student'),
        ),
    ]
