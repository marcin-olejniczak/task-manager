from django.conf.urls import include, url
from django.contrib import admin
from .views import TaskCreate, TaskUpdate

urlpatterns = [
    url(r'^login/$', 'core.views.login_user', name='login_user'),
    url(r'^logout/$', 'core.views.logout_user', name='logout_user'),
    url(r'^$', 'core.views.home', name='home'),
    url(r'^project/', 'core.views.project', name='project'),
    url(
        r'^project/(?P<id>[0-9]+)/',
        'core.views.project',
        name='project'
    ),
    url(r'^project/edit/', 'core.views.project_edit', name='project_edit'),
    url(
        r'^project/edit/(?P<id>[0-9]+)/',
        'core.views.project_edit',
        name='project_edit'
    ),
    url(r'^task/add/', TaskCreate.as_view(), name='task'),
    url(
        r'^task/update/(?P<pk>[0-9]+)$',
        TaskUpdate.as_view(),
        name='task_update'
    ),
]
