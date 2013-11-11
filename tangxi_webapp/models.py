#coding=utf-8
from django.db import models
# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length=50, verbose_name=u'姓名')
	gender = models.IntegerField(verbose_name=u'性别')
	thumbnail = models.FileField(upload_to='employee_thumbnails/', verbose_name=u'照片')

	class Meta:
		verbose_name = '员工'
		verbose_name_plural = '员工'

	def __unicode__(self):
		return self.name;

class Activity(models.Model):
	name = models.CharField(max_length=100, verbose_name=u'名称')
	date  = models.DateField(auto_now=False, auto_now_add=True, verbose_name=u'日期')
	description = models.CharField(max_length=5000, verbose_name=u'新闻内容')

	class Meta:
		verbose_name = '企业新闻'
		verbose_name_plural = '企业新闻'

	def __unicode__(self):
		return self.name;

class Images(models.Model):
	title = models.CharField(max_length=100, verbose_name=u'图片名称')
	date = models.DateField(auto_now=False, auto_now_add=True, verbose_name=u'日期')
	path = models.FileField(upload_to='share/', verbose_name=u'图片路径')
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = '图片'
		verbose_name_plural = '图片'

	def __unicode__(self):
		return self.title;


class ServiceProfile(models.Model):
	name = models.CharField(max_length=100, verbose_name=u'服务名称')
	image_title = models.CharField(max_length=100, verbose_name=u'图片名称')
	description = models.TextField(verbose_name=u'服务描述')

	class Meta:
		verbose_name = '服务基本信息'
		verbose_name_plural = '服务基本信息'

	def __unicode__(self):
		return self.name;

class Jobs(models.Model):
	title = models.CharField(max_length=100, verbose_name=u'职位名称')
	date = models.DateField(auto_now=False, auto_now_add=True, verbose_name=u'发布日期')
	quantity = models.IntegerField(verbose_name=u'招聘数量')
	description = models.TextField(verbose_name=u'职位招聘描述')

	class Meta:
		verbose_name = '工作机会'
		verbose_name_plural = '工作机会'

	def __unicode__(self):
		return self.title;