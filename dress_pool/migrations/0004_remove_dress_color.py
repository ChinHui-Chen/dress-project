# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dress_pool', '0003_auto_20150705_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dress',
            name='color',
        ),
    ]
