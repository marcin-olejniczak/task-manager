from django.conf.urls import include, url
from django.contrib import admin
from .views import (
    TaskCreateView, TaskUpdateView, TaskPreviewView,
    ProjectCreateView, ProjectUpdateView, ProjectPreviewView)

urlpatterns = [
    url(r'^login/$', 'core.views.login_user', name='login_user'),
    url(r'^logout/$', 'core.views.logout_user', name='logout_user'),
    url(r'^$', 'core.views.home', name='home'),
    url(r'^project/$', 'core.views.project', name='project'),
    url(r'^project/add/$', ProjectCreateView.as_view(), name='project_create'),
    url(
        r'^project/update/(?P<pk>[0-9]+)$',
        ProjectUpdateView.as_view(),
        name='project_update'
    ),
    url(
        r'^project/preview/(?P<pk>[0-9]+)$',
        ProjectPreviewView.as_view(),
        name='project_preview'
    ),
    url(r'^task/$', 'core.views.task', name='task'),
    url(r'^task/add/$', TaskCreateView.as_view(), name='task_create'),
    url(
        r'^task/update/(?P<pk>[0-9]+)$',
        TaskUpdateView.as_view(),
        name='task_update'
    ),
    url(
        r'^task/preview/(?P<pk>[0-9]+)$',
        TaskPreviewView.as_view(),
        name='task_preview'
    ),
]
