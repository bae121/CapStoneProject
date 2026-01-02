from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User, Goal
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, GoalSerializer, DailyNotesSerializer, WeeklySummarySerializer

def home(request): 
    return render(request, 'notes/home.html')

# Register new users
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# Login users and return token
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": UserSerializer(user).data
        })


# Goals: list and create
class GoalListCreateView(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Goals: retrieve, update, delete
class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)


# Daily Notes: retrieve and update
class DailyNotesView(generics.RetrieveUpdateAPIView):
    serializer_class = DailyNotesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# Weekly Summary: retrieve and update
class WeeklySummaryView(generics.RetrieveUpdateAPIView):
    serializer_class = WeeklySummarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class CustomLoginView(LoginView):
    template_name = 'notes/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'notes/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'notes/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        request.user.daily_notes = request.POST.get('daily_notes')
        request.user.weekly_summary = request.POST.get('weekly_summary')
        request.user.save()
    return render(request, 'notes/profile.html', {'user': request.user})
