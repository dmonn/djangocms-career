# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_career', '0003_auto_20160418_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_active',
            new_name='active_post',
        ),
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=True, help_text="This flag will make the position public. Don't tick this if you want to make a draft.", verbose_name='Is public?'),
            preserve_default=False,
        ),
    ]
