# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicvis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='instrumentos',
            field=models.ManyToManyField(to='musicvis.Instrumentos', blank=True),
        ),
        migrations.RemoveField(
            model_name='clasesmusica',
            name='alumno',
        ),
        migrations.AddField(
            model_name='clasesmusica',
            name='alumno',
            field=models.ManyToManyField(to='musicvis.Alumnos'),
        ),
    ]
