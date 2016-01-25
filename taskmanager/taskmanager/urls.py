from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^login/$', 'core.views.login', name='login'),
    url(r'^logout/$', 'core.views.logout_user', name='logout_user'),
    url(r'^$', 'core.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
