# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160128_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'new', max_length=30, choices=[(b'new', b'New'), (b'closed', b'Closed'), (b'feedback', b'Feedback'), (b'in_progress', b'In Progress')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
