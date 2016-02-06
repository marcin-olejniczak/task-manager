from django.conf.urls import include, url
from django.contrib import admin
from .views import TaskCreate, TaskUpdate, ProjectCreate, ProjectUpdate

urlpatterns = [
    url(r'^login/$', 'core.views.login_user', name='login_user'),
    url(r'^logout/$', 'core.views.logout_user', name='logout_user'),
    url(r'^$', 'core.views.home', name='home'),
    url(r'^project/$', 'core.views.project', name='project'),
    url(r'^project/add/', ProjectCreate.as_view(), name='project_create'),
    url(
        r'^project/update/(?P<pk>[0-9]+)$',
        ProjectUpdate.as_view(),
        name='project_update'
    ),
    url(r'^task/$', 'core.views.task', name='task'),
    url(r'^task/add/', TaskCreate.as_view(), name='task_create'),
    url(
        r'^task/update/(?P<pk>[0-9]+)$',
        TaskUpdate.as_view(),
        name='task_update'
    ),
]
