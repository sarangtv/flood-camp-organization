# Generated by Django 3.1.2 on 2020-12-12 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_victim_details_health_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='camp_organizer_registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='user_registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='volunteer_registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('role', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
            ],
        ),
    ]
