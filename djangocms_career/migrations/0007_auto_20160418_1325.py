# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_career', '0006_remove_post_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(help_text='Give a short description about your work and responsibilities.', max_length=2048, null=True, verbose_name='Description', blank=True),
        ),
    ]
