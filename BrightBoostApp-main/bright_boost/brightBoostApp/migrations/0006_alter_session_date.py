# Generated by Django 4.2.4 on 2023-10-08 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brightBoostApp', '0005_session_instructor_session_room_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
