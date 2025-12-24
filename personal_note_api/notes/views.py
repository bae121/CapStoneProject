from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import User, Goal
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, GoalSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


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