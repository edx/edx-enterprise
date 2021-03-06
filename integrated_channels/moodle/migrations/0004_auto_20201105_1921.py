# Generated by Django 2.2.16 on 2020-11-05 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moodle', '0003_auto_20201006_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmoodleenterprisecustomerconfiguration',
            name='transmission_chunk_size',
            field=models.IntegerField(default=1, help_text='The maximum number of data items to transmit to the integrated channel with each request.'),
        ),
        migrations.AlterField(
            model_name='moodleenterprisecustomerconfiguration',
            name='transmission_chunk_size',
            field=models.IntegerField(default=1, help_text='The maximum number of data items to transmit to the integrated channel with each request.'),
        ),
    ]
