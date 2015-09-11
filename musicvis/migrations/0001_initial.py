# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('ci', models.IntegerField()),
                ('nivel', models.CharField(max_length=200, choices=[(b'i', b'Inicial'), (b'ba', b'Basico'), (b'in', b'Intermedio'), (b'av', b'Avanzado')])),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='ClasesMusica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_inicio', models.DateTimeField()),
                ('hora_salida', models.DateTimeField()),
                ('costo', models.IntegerField()),
                ('alumno', models.ForeignKey(to='musicvis.Alumnos')),
            ],
            options={
                'verbose_name': 'Clase de m\xfasica',
                'verbose_name_plural': 'Clases de m\xfasica',
            },
        ),
        migrations.CreateModel(
            name='Instrumentos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200, choices=[(b'Cu', b'Cuerda'), (b'Vi', b'Viento'), (b'Pe', b'Percusion'), (b'Ot', b'Otros')])),
            ],
            options={
                'verbose_name': 'Instrumento',
                'verbose_name_plural': 'Instrumentos',
            },
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('ci', models.IntegerField()),
                ('experiencia', models.IntegerField()),
                ('instrumentos', models.ManyToManyField(to='musicvis.Instrumentos')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.AddField(
            model_name='clasesmusica',
            name='instrumento',
            field=models.ForeignKey(to='musicvis.Instrumentos'),
        ),
        migrations.AddField(
            model_name='clasesmusica',
            name='profesor',
            field=models.ForeignKey(to='musicvis.Profesores'),
        ),
        migrations.AddField(
            model_name='alumnos',
            name='instrumentos',
            field=models.ManyToManyField(to='musicvis.Instrumentos'),
        ),
    ]
