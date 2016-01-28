# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160128_2206'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='projectmember',
            unique_together=set([('user', 'project')]),
        ),
    ]
