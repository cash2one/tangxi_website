# -*- coding: utf-8 -*- 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from .models import *
from tangxi_website.settings import *
from django.core.context_processors import csrf
from django.core.mail import send_mail
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
		

#=======================================
# Function APIs:
#---------------------------------------
def show_enter_page(request):
	'''
	/
	a beatiful entrance page
	'''
	return render(request, 'tangxi_webapp/home.html',{})

def show_home_page(request):
	'''
	'''
	return render(request, 'tangxi_webapp/home.html',{'active_menu':'/home/'})

def show_news_page(request, page_number=1):
	'''
	'''
	news = Activity.objects.all().order_by('-date')
	p = Paginator(news, 3)
	page = p.page(page_number)
	news_in_page = page.object_list
	context = {
		'active_menu':'/news/',
		'news':news_in_page,
		'page':page,
		'paginator':p
	}
	return render(request, 'tangxi_webapp/news.html', context)

#id is numeric
def show_news_detail_page(request, news_id):
	'''
	'''
	news_detail = get_object_or_404(Activity, id=news_id)
	return render(request, 'tangxi_webapp/news_detail.html',{'active_menu':'/news/', 'news_detail':news_detail})

def show_company_culture_page(request):
	'''
	'''
	img_url = MEDIA_URL
	imgs = Images.objects.all()[:4]
	context = {
		'active_menu':'/company_culture/',
		'img_url':img_url,
		'imgs':imgs
	}
	return render(request, 'tangxi_webapp/company_culture.html', context)

service_dictionary = {}
service_dictionary['foot_massage'] = u'足疗按摩'
service_dictionary['tea'] = u'茶道'
service_dictionary['card'] = u'棋牌'
service_dictionary['spa'] = u'SPA'
service_dictionary['billiard'] = u'台球'

def show_services_page(request, service_name=''):
	'''
	'''
	img_url = ''
	description = ''
	if service_name == '':
		return render(request, 'tangxi_webapp/services.html',{'active_menu':'/services/'})
	try:
		img = Images.objects.get(title=service_name)
		img_url = MEDIA_URL + img.path.name
		service_profile = ServiceProfile.objects.get(name=service_name)
		service_display_name = service_dictionary[service_name]
		description = service_profile.description
	except Images.DoesNotExist, ServiceProfile.DoesNotExist:
		pass
	banner_img = "banner_%s.jpg" % (service_name)
	imgs = []
	for x in xrange(1,4):
		imgs.append("%s_%d.jpg" % (service_name, x))
	context = {
		'active_menu':'/services/',
		'service_display_name': service_display_name,
		'img_url':img_url,
		'description':description,
		'banner_img':banner_img, 
		'imgs':imgs
	}
	return render(request, 'tangxi_webapp/services_detail.html', context)

def show_contact_page(request):
	'''
	'''
	c = {'active_menu':'/contact/'}
	c.update(csrf(request))
	if request.method == 'POST':
		name = request.POST['name']
		contact_info = request.POST['contact']
		msg = request.POST['message']
		content = '姓名: %s\n联系方式: %s\n留言: \n%s' % (name, contact_info, msg)
		send_mail(
			'客户留言反馈', # subject
			content, # message
			EMAIL_HOST_USER, # from email
			[EMAIL_HOST_USER], # recipient_list
		)
		return HttpResponseRedirect('/thanks/')
	return render(request, 'tangxi_webapp/contact.html', c)

def show_contact_thanks_page(request):
	return render(request, 'tangxi_webapp/thanks.html', {})

def show_join_us_page(request, page_number=1):
	'''
	'''
	jobs = Jobs.objects.all().order_by('-date')
	p = Paginator(jobs, 3)
	page = p.page(page_number)
	jobs_in_page = page.object_list
	context = {
		'jobs':jobs_in_page,
		'page':page,
		'paginator':p
	}
	return render(request, 'tangxi_webapp/join_us.html', context)

def show_example_page(request):
	'''
	'''
	return render(request, 'tangxi_webapp/example.html', {})


def show_about_page(request):
	'''
	/about/
	show the about page
	'''
	return render(request, 'tangxi_webapp/about.html',{'active_menu':'/about/'}) 

def show_photos_page(request):
	'''
	'''
	return render(request, 'tangxi_webapp/photos.html', {}) 

#=======================================
# Function API End Here.
#---------------------------------------