from django import forms
from .models import Session, TutorSchedule, Students, Question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# The SessionForm class is a ModelForm that is used to create or update Session objects with specified
# fields.
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['date','session_time','room_no','instructor', 'students_attended', 'subject_area']

# The QuestionForm class is a form that allows users to input information about a tutor's
# questions.
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_no','question_asked','question_answered','instructor','subject_area']

# The TutorScheduleForm class is a form that allows users to input information about a tutor's
# schedule.
class TutorScheduleForm(forms.ModelForm):
    class Meta:
        model = TutorSchedule
        fields = ['tutor_name', 'day_of_week', 'start_time', 'end_time','room','subject_area']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_id','student_name','student_email']

# The `CustomRegistrationForm` class is a subclass of `UserCreationForm` that adds a `user_role` field
# with choices for teacher, student, and head.

class CustomRegistrationForm(UserCreationForm):
    USER_ROLES = (
        ('teacher', 'Teacher'),
        # ('staff', 'Staff'),
        ('admin', 'Admin'),
    )
    user_role = forms.ChoiceField(choices=USER_ROLES)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'user_role')
