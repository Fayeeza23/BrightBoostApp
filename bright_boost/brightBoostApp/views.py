
# Create views here.

from django.shortcuts import render, redirect
from .models import Session, TutorSchedule
from .forms import SessionForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group 
from .forms import CustomRegistrationForm
from django.contrib.auth.models import User, Group 
from django.contrib.auth import login as auth_login, logout as auth_logout


@login_required
def dashboardView(request):
    return render (request,'dashboard.html')


def home(request):
    return render(request,'index.html')

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
            elif user_role == 'student':
                user.groups.add(Group.objects.get(name='Student'))
            elif user_role == 'staff':
                user.groups.add(Group.objects.get(name='Staff'))

            # Log in the user after registration
            auth_login(request, user)
            if user_role == 'student':
                return redirect('display_timetable')  # Redirect to the dashboard or any other desired URL after registration
    else:
        form = CustomRegistrationForm()

    return render(request, 'registration.html', {'form': form})


def display_timetable(request):
    tutor_schedules = TutorSchedule.objects.all()
    return render(request, 'display_timetable.html', {'tutor_schedules': tutor_schedules})

def homepage(request):
    tutor_schedules = TutorSchedule.objects.all()
    return render(request, 'home.html', {'tutor_schedules': tutor_schedules})


def add_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessions_list')
    else:
        form = SessionForm()
    return render(request, 'add_session.html', {'form': form})

def sessions_list(request):
    sessions = Session.objects.all()  # Retrieve all session objects from the database
    return render(request, 'sessions_list.html', {'sessions': sessions})


