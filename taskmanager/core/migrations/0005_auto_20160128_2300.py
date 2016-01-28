# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160128_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(default=b'Normal', max_length=30, choices=[(b'Low', b'Low'), (b'Normal', b'Normal'), (b'High', b'High'), (b'Urgent', b'Urgent')]),
        ),
    ]
