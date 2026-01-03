from django.urls import path
from notes.views import (
    APIRegisterView, APILoginView, GoalListCreateView, GoalDetailView,
    DailyNotesView, WeeklySummaryView,
    CustomLoginView, CustomLogoutView,
    register, profile, home
)

urlpatterns = [
    # Template-based views
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # API endpoints
    path('api/register/', APIRegisterView.as_view(), name='api-register'),
    path('api/login/', APILoginView.as_view(), name='api-login'),
    path('api/goals/', GoalListCreateView.as_view(), name='goal-list-create'),
    path('api/goals/<int:pk>/', GoalDetailView.as_view(), name='goal-detail'),
    path('api/daily-notes/', DailyNotesView.as_view(), name='daily-notes'),
    path('api/weekly-summary/', WeeklySummaryView.as_view(), name='weekly-summary'),
]
