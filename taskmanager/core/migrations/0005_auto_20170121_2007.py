# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160210_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tracked_tasks',
            field=models.ManyToManyField(related_name='tracked_tasks', to='core.Task', blank=True),
        ),
    ]
