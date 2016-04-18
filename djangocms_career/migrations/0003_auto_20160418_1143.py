# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('djangocms_career', '0002_positionplugin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('start_date', models.DateField(help_text='The date when you started this position - only the month and year will be displayed', verbose_name='Start date')),
                ('end_date', models.DateField(help_text="The date when this position ended - only the month and year will be displayed. You don't have to define this if it is your active post.", null=True, verbose_name='End date', blank=True)),
                ('is_active', models.BooleanField(help_text="Check this if this is your active post. You won't have to add the end_date in that case.", verbose_name='Active position?')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('company', models.CharField(max_length=255, verbose_name='Company')),
                ('description', models.TextField(help_text='Give a short description about your work and responsibilities.', max_length=2048, null=True, verbose_name='Description', blank=True)),
                ('website', models.CharField(help_text="Provide a link to the company's website.", max_length=255, verbose_name='Website')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='positionplugin',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='positionplugin',
            name='post',
        ),
        migrations.AlterUniqueTogether(
            name='positiontranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='positiontranslation',
            name='master',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.DeleteModel(
            name='PositionPlugin',
        ),
        migrations.DeleteModel(
            name='PositionTranslation',
        ),
    ]
