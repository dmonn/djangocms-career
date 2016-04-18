# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(help_text='The date when you started this position - only the month and year will be displayed', verbose_name='Start date')),
                ('end_date', models.DateField(help_text="The date when this position ended - only the month and year will be displayed. You don't have to define this if it is your active post.", null=True, verbose_name='End date', blank=True)),
                ('is_active', models.BooleanField(help_text="Check this if this is your active post. You won't have to add the end_date in that case.", verbose_name='Active position?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PositionTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('company', models.CharField(max_length=255, verbose_name='Company')),
                ('description', models.TextField(help_text='Give a short description about your work and responsibilities.', max_length=2048, null=True, verbose_name='Description', blank=True)),
                ('website', models.CharField(help_text="Provide a link to the company's website.", max_length=255, verbose_name='Website')),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='djangocms_career.Position', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'djangocms_career_position_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='positiontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
