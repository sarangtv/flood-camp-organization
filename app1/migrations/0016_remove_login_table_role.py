# Generated by Django 3.1.2 on 2020-12-09 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_flood_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login_table',
            name='role',
        ),
    ]
