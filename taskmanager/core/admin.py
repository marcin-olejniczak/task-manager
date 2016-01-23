from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import *

admin.site.register(Change)
admin.site.register(ChangeDetail)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Role)
admin.site.register(Task)
admin.site.register(UserProfile)

