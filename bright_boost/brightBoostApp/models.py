from django.db import models

# Create your models here.
# class Tutor(models.Model):
#   firstName = models.CharField(max_length=255)
#   lastName = models.CharField(max_length=255)
#   subjectName = models.CharField(max_length=255)

from django.utils import timezone
from datetime import date
class Session(models.Model):
    date = models.DateField()
    session_time = models.TimeField()
    room_no =models.CharField(max_length=80)
    instructor = models.CharField(max_length=100 )
    students_attended = models.PositiveIntegerField()
    questions_answered = models.PositiveIntegerField()
    subject_area = models.CharField(max_length=100)

class TutorSchedule(models.Model):
    tutor_name = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room= models.CharField(max_length=80)
