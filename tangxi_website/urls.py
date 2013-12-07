from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.static import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# required to make static serving work
	#(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	# Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('tangxi_webapp.views',
	url(r'^$', 'show_enter_page'),
    url(r'^home/$', 'show_home_page'),
    url(r'^news/$', 'show_news_page'),
    url(r'^news/(?P<page_number>\d+)/$', 'show_news_page'),
    url(r'^news_detail/(?P<news_id>\d+)/$', 'show_news_detail_page'),
    url(r'^company_culture/$', 'show_company_culture_page'),
    url(r'^services/(?P<service_name>\w+)/$', 'show_services_page'),
    url(r'^services/$', 'show_services_page'),

    url(r'^thanks/$', 'show_contact_thanks_page'),
    url(r'^contact/$', 'show_contact_page'),
    #url(r'^about/$', 'show_about_page'),
    url(r'^join_us/(?P<page_number>\d+)/$', 'show_join_us_page'),
    url(r'^join_us/$', 'show_join_us_page'),
    #url(r'^photos/$', 'show_photos_page'),
    
	
)

if settings.DEBUG:
	urlpatterns += patterns('',
#		(r'^debuginfo/$', tangxi_webapp.views.debug),
	)
