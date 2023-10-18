from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('',views.homepage,name='home'),
    path('register/', views.registerView, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('dashboard/', views.dashboardView, name='dashboard'),

# Admin
    path('view_user/', views.viewUser, name='view_user'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_tutor/', views.add_tutor, name='add_tutor'),
    path('weekly_session_statistics/',views.weekly_session_statistics,name='weekly_session_statistics'),

# Tutor
    path('add_session/', views.add_session, name='add_session'),
    path('sessions_list/', views.sessions_list, name='sessions_list'),
    path('add_question/', views.add_question, name='add_question'),


]
