# Generated by Django 5.1.1 on 2024-10-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_userdata_password'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_user_permissions_set', to='auth.permission'),
        ),
    ]
