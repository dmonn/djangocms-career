# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_career', '0007_auto_20160418_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='website',
            field=models.CharField(help_text="Provide a link to the company's website.", max_length=255, null=True, verbose_name='Website', blank=True),
        ),
    ]
