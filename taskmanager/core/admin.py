from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import *


class ChangeAdmin(admin.ModelAdmin):
    list_display = ('modified_date',)
    search_fields = []


class ChangeDetailAdmin(admin.ModelAdmin):
    list_display = ('modified_date',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']


class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('get_user_login', 'get_project_name')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Change, ChangeAdmin)
admin.site.register(ChangeDetail, ChangeDetailAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMember, ProjectMemberAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(UserProfile)
