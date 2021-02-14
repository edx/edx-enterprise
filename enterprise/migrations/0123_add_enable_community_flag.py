# Generated by Django 2.2.18 on 2021-02-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0122_remove_field_sync_enterprise_catalog_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='enable_community',
            field=models.BooleanField(default=False, help_text='Specifies whether the Community feature should be enabled for this Enterprise Customer.'),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='enable_community',
            field=models.BooleanField(default=False, help_text='Specifies whether the Community feature should be enabled for this Enterprise Customer.'),
        ),
    ]