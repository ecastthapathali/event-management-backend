# Generated by Django 5.1.1 on 2024-10-01 13:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_eventreg_event_id_eventreg_event_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventreg',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='eventreg',
            name='participant_id',
        ),
        migrations.AddField(
            model_name='eventreg',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.eventmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventreg',
            name='participant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
