# Generated by Django 4.2.4 on 2023-10-08 08:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brightBoostApp', '0004_alter_tutorschedule_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='instructor',
            field=models.CharField(default='Unknown Instructor', max_length=100),
        ),
        migrations.AddField(
            model_name='session',
            name='room_no',
            field=models.CharField(default='Unknown Room', max_length=80),
        ),
        migrations.AddField(
            model_name='session',
            name='session_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
