# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_career', '0005_auto_20160418_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_public',
        ),
    ]
