from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout

from .models import Goal
from .serializers import (
    RegisterSerializer, LoginSerializer, UserSerializer,
    GoalSerializer, DailyNotesSerializer, WeeklySummarySerializer
)


# --- HOME ---
class HomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Welcome to Personal Note Project"})


# --- PROFILE ---
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return user profile data."""
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        """Update daily notes and weekly summary."""
        request.user.daily_notes = request.data.get("daily_notes", request.user.daily_notes)
        request.user.weekly_summary = request.data.get("weekly_summary", request.user.weekly_summary)
        request.user.save()
        return Response({"message": "Profile updated successfully"})


# --- REGISTER ---
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "message": "User registered successfully",
                "user": UserSerializer(user).data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- LOGIN ---
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)  # Django session login (optional)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            "message": "Login successful",
            "user": UserSerializer(user).data,
            "token": token.key
        })


# --- LOGOUT ---
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})


class GoalListCreateView(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)


class DailyNotesView(generics.RetrieveUpdateAPIView):
    serializer_class = DailyNotesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class WeeklySummaryView(generics.RetrieveUpdateAPIView):
    serializer_class = WeeklySummarySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user