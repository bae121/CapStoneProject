"""
URL configuration for personal_note_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from notes.views import RegisterView, LoginView, GoalListCreateView, GoalDetailView, DailyNotesView, WeeklySummaryView, CustomLoginView, CustomLogoutView, register, profile, home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    path('api/register/', RegisterView.as_view(), name='register'), 
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/goals/', GoalListCreateView.as_view(), name='goal-list-create'), 
    path('api/goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    path('api/daily-notes/', DailyNotesView.as_view(), name='daily-notes'), 
    path('api/weekly-summary/', WeeklySummaryView.as_view(), name='weekly-summary'), 

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    path('', include('notes.urls')),
]