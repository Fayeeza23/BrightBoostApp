# Create views here.
from django.shortcuts import render, redirect
from .models import Question, Session, TutorSchedule, Students
from .forms import QuestionForm, SessionForm, StudentForm, TutorScheduleForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group 
from .forms import CustomRegistrationForm
from django.contrib.auth.models import User, Group 
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.db.models import Sum
from django.db.models.functions import TruncWeek


@login_required
def dashboardView(request):
    user = request.user
    user_groups = user.groups.values_list('name', flat=True)  # Get a list of user's group names
    if 'Admin' in user_groups:
        # User is in the 'Admin' group
        return render(request, 'admin_dashboard.html')
    elif 'Teacher' in user_groups:
        # User is in the 'Teacher' group
        return render(request, 'teacher_dashboard.html')

# App Homepage
def homepage(request):
    tutor_schedules = TutorSchedule.objects.all()
    return render(request, 'home.html', {'tutor_schedules': tutor_schedules})

# Registration Page
@login_required
def registerView(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user_role = form.cleaned_data['user_role']

            # Create a user with the provided data
            user = User.objects.create_user(username=username, password=password)
            # Add the user to the selected group based on the user_role
            if user_role == 'teacher':
                user.groups.add(Group.objects.get(name='Teacher'))
            elif user_role == 'admin':
                user.groups.add(Group.objects.get(name='Admin'))
    else:
        form = CustomRegistrationForm()

    return render(request, 'registration.html', {'form': form})

# Add Session Page 
@login_required
def add_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessions_list')
    else:
        form = SessionForm()
    return render(request, 'add_session.html', {'form': form})

# Show Session Page
@login_required
def sessions_list(request):
    sessions = Session.objects.all()  # Retrieve all session objects from the database
    question = Question.objects.all()
    context = {
        'sessions': sessions,
        'question' : question
    }
    return render(request, 'sessions_list.html', context)
    
# Add Session Page 
@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessions_list')
    else:
        form = QuestionForm()
    return render(request, 'question.html', {'form': form})

# Admin
def viewUser(request):
    tutor = Session.objects.all()  # Retrieve all session objects from the database
    students = Students.objects.all()  
    context = {
        'tutor': tutor,
        'students':  students,
    }
    return render(request, 'view_user.html', context)

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_user')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

@login_required
def add_tutor(request):
    if request.method == 'POST':
        form = TutorScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessions_list')
    else:
        form = TutorScheduleForm()
    return render(request, 'add_tutor.html', {'form': form})


@login_required
def weekly_session_statistics(request):
    # Group sessions by week and calculate the sum of students attended
    weekly_stats = Session.objects.annotate(week=TruncWeek('date')).values('week').annotate(total_students=Sum('students_attended')).order_by('week')
    instructor= Session.objects.values('instructor').annotate(total_students=Sum('students_attended')).order_by('instructor').all()
    subjects = Session.objects.all()

    return render(request, 'weekly_statistics.html', {'weekly_stats': weekly_stats, 'subjects': subjects,'instructor': instructor})

