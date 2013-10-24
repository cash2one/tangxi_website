#coding=utf-8
from django.db import models
# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=50)
	gender = models.IntegerField()
	thumbnail = models.FileField(upload_to='employee_thumbnails/')

class Activity(models.Model):
	name = models.CharField(max_length=100)
	date  = models.DateField(auto_now=False, auto_now_add=True)
	description = models.CharField(max_length=5000)

class Images(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField(auto_now=False, auto_now_add=True)
	path = models.FileField(upload_to='share/')
	def __unicode__(self):
		return self.title

class ServiceProfile(models.Model):
	name = models.CharField(max_length=100)
	image_title = models.CharField(max_length=100)
	description = models.TextField()

class Jobs(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField(auto_now=False, auto_now_add=True)
	quantity = models.IntegerField()
	description = models.TextField()