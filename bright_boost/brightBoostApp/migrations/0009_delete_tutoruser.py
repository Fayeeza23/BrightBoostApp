# Generated by Django 4.2.4 on 2023-10-09 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brightBoostApp', '0008_remove_tutoruser_day_of_week_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TutorUser',
        ),
    ]
