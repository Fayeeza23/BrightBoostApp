# Generated by Django 4.2.4 on 2023-10-13 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brightBoostApp', '0012_tutorschedule_subject_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorschedule',
            name='subject_area',
            field=models.CharField(max_length=100),
        ),
    ]