from django.contrib import admin
from tangxi_webapp.models import *

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('name', 'gender', 'thumbnail',)
	list_filter = ('name', 'gender', 'thumbnail',)
	ordering = ('-name',)
	fields = ('name', 'gender', 'thumbnail',)

class ActivityAdmin(admin.ModelAdmin):
	list_display = ('name', 'date', 'description',)
	list_filter = ('name', 'date', 'description',)
	ordering = ('-name',)

class ImagesAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'path',)
	list_filter = ('title', 'date', 'path',)
	ordering = ('-title',)
	fields = ('title', 'path',)

class ServiceProfileAdmin(admin.ModelAdmin):
	list_display = ('name', 'image_title', 'description',)
	list_filter = ('name', 'image_title',)
	ordering = ('-name',)
	fields = ('name', 'image_title', 'description')

class JobsAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'quantity', 'description')
	list_filter = ('title', 'date', 'quantity')
	ordering = ('-title', '-date', '-quantity')
	fields = ('title', 'quantity', 'description')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(ServiceProfile, ServiceProfileAdmin)
admin.site.register(Jobs, JobsAdmin)