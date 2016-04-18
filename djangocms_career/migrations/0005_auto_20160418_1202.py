# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_career', '0004_auto_20160418_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='active_post',
            field=models.BooleanField(help_text="Check this if this is your active post. You won't have to add the end date in that case.", verbose_name='Active position?'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(help_text='Give a short description about your work and responsibilities.', max_length=2048, null=True, verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=True, help_text="This flag will make the position public. Don't tick this if you want to make a draft.", verbose_name='Is public?'),
        ),
    ]
