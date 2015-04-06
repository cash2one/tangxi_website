from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('tangxi_webapp.urls', namespace="main")),
    url(r'^admin/', include(admin.site.urls)),
]

