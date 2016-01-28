# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160128_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'new', max_length=30, choices=[(b'low', b'Low'), (b'normal', b'Normal'), (b'high', b'High'), (b'urgent', b'Urgent')]),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default=b'normal', max_length=30, choices=[(b'low', b'Low'), (b'normal', b'Normal'), (b'high', b'High'), (b'urgent', b'Urgent')]),
        ),
    ]
