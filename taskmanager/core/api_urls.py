from django.conf.urls import patterns, include, url
from api_views import task_toggle_tracking

urlpatterns = [
    url(
        r'^task/task_toggle_tracking/(?P<pk>[0-9]+)$',
        task_toggle_tracking,
        name='task_toggle_tracking'
    ),
]