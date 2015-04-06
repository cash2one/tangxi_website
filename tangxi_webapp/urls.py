from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.show_enter_page, name='show_enter_page'),
    url(r'^home/$', views.show_home_page, name='show_home_page'),
    url(r'^news/$', views.show_news_page, name='show_news_page'),
    url(r'^news/(?P<page_number>\d+)/$', views.show_news_page, name='show_news_page'),
    url(r'^news_detail/(?P<news_id>\d+)/$', views.show_news_detail_page, name='show_news_detail_page'),
    url(r'^company_culture/$', views.show_company_culture_page, name='show_company_culture_page'),
    url(r'^services/(?P<service_name>\w+)/$', views.show_services_page, name='show_services_page'),
    url(r'^services/$', views.show_services_page, name='show_services_page'),

    url(r'^thanks/$', views.show_contact_thanks_page, name='show_contact_thanks_page'),
    url(r'^contact/$', views.show_contact_page, name='show_contact_page'),
    #url(r'^about/$', 'show_about_page'),
    url(r'^join_us/(?P<page_number>\d+)/$', views.show_join_us_page, name='show_join_us_page'),
    url(r'^join_us/$', views.show_join_us_page, name='show_join_us_page'),
    #url(r'^photos/$', 'show_photos_page'),
]  