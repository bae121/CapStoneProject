from django.urls import path
from notes.views import RegisterView, LoginView, GoalListCreateView, GoalDetailView, DailyNotesView, WeeklySummaryView, CustomLoginView, CustomLogoutView, register, profile, home

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]
