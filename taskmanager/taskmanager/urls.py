from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^login/$', 'core.views.login_user', name='login_user'),
    url(r'^logout/$', 'core.views.logout_user', name='logout_user'),
    url(r'^$', 'core.views.home', name='home'),
    url(r'^project/edit/', 'core.views.project_edit', name='project_edit'),
    url(
        r'^project/edit/(?P<id>[0-9]+)/',
        'core.views.project_edit',
        name='project_edit'),
    url(r'^project/', 'core.views.project', name='project'),
    url(
        r'^project/(?P<id>[0-9]+)/',
        'core.views.project',
        name='project'),
    url(r'^task/edit/', 'core.views.task_edit', name='task_edit'),
    url(
        r'^task/edit/(?P<id>[0-9]+)/',
        'core.views.task_edit',
        name='task_edit'),
    url(r'^task/', 'core.views.task', name='task'),
    url(
        r'^task/(?P<id>[0-9]+)/',
        'core.views.task',
        name='task'),
    url(r'^admin/', include(admin.site.urls)),
]
