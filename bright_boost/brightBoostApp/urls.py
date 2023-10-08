from django.urls import path
from . import views

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.homepage,name='home'),
    path('register/', views.registerView, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('timetable/', views.display_timetable, name='timetable'),

    # path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='home'), name="logout"),
    path('add_session/', views.add_session, name='add_session'),
    path('sessions_list/', views.sessions_list, name='sessions_list')
  
    # Define other URL patterns here
]
