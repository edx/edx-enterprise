# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-05 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0088_auto_20200224_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprisecustomerreportingconfiguration',
            name='data_type',
            field=models.CharField(choices=[('progress', 'progress'), ('progress_v2', 'progress_v2'), ('catalog', 'catalog'), ('engagement', 'engagement')], default='progress', help_text='The type of data this report should contain.', max_length=20, verbose_name='Data Type'),
        ),
    ]
