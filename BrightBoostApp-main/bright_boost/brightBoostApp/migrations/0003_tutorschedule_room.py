# Generated by Django 4.2.4 on 2023-10-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brightBoostApp', '0002_session_tutorschedule_delete_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorschedule',
            name='room',
            field=models.CharField(default='Default Room Value', max_length=80),
        ),
    ]