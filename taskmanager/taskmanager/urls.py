from django.conf.urls import include, url
from django.contrib import admin
from core import urls as core_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(core_urls)),
]
