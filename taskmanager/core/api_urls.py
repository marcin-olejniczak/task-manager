from django.conf.urls import patterns, include, url
from api_views import task_toggle_tracking, comment_create, comments_get

urlpatterns = [
    url(
        r'^task/toggle_tracking/(?P<pk>[0-9]+)$',
        task_toggle_tracking,
        name='task_toggle_tracking'
    ),
    url(
        r'^comment/create/(?P<task_id>[0-9]+)$',
        comment_create,
        name='comment_create'
    ),
    url(
        r'^comments/get/(?P<task_id>[0-9]+)$',
        comments_get,
        name='comments_get'
    ),
]