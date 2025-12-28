from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Goal

class GoalSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Goal 
        fields = ['id', 'title', 'description', 'created_at'] 
        read_only_fields = ['id', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    goals = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'daily_notes', 'weekly_summary', 'goals']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            data['user'] = user
            return data
        raise serializers.ValidationError("Invalid credentials")


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials")

class DailyNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['daily_notes']
        extra_kwargs = {'daily_notes': {'required': False}}

        

class WeeklySummarySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['weekly_summary']