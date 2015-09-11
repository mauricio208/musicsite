# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
class Instrumentos(models.Model):
	TIPO_INSTRUMENTO=(
			("Cu","Cuerda"),
			("Vi","Viento"),
			("Pe","Percusion"),
			("Ot","Otros"),
		)
	nombre=models.CharField(max_length=200)
	tipo=models.CharField(max_length=200,choices=TIPO_INSTRUMENTO)

	class Meta:
		verbose_name = "Instrumento"
		verbose_name_plural = "Instrumentos"

	def __unicode__(self):
		return self.nombre


class Alumnos(models.Model):
	NIVELES=(
			("i","Inicial"),
			("ba","Basico"),
			("in","Intermedio"),
			("av","Avanzado"),
		)
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	ci=models.IntegerField()
	instrumentos=models.ManyToManyField(Instrumentos,blank=True)
	nivel=models.CharField(max_length=200,choices=NIVELES)

	class Meta:
	    verbose_name = "Alumno"
	    verbose_name_plural = "Alumnos"

	def __unicode__(self):
		return self.nombre+self.apellido
    

class Profesores(models.Model):
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	ci=models.IntegerField()
	instrumentos=models.ManyToManyField(Instrumentos)
	experiencia=models.IntegerField()

	class Meta:
	    verbose_name = "Profesor"
	    verbose_name_plural = "Profesores"

	def __unicode__(self):
		return self.nombre+' '+self.apellido


class ClasesMusica(models.Model):
	"""Representa las clases dadas en el centro musical"""
	profesor=models.ForeignKey(Profesores)
	alumno=models.ManyToManyField(Alumnos)
	hora_inicio=models.DateTimeField()
	hora_salida=models.DateTimeField()
	instrumento=models.ForeignKey(Instrumentos)
	costo=models.IntegerField()

	class Meta:
	    verbose_name = u"Clase de música"
	    verbose_name_plural = u"Clases de música"

	def __unicode__(self):
		return 'Clase de '+self.instrumento.nombre