# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofile_tracked_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmember',
            name='project',
            field=models.ForeignKey(related_name='project_member', to='core.Project'),
        ),
        migrations.AlterField(
            model_name='projectmember',
            name='user',
            field=models.ForeignKey(related_name='project_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
