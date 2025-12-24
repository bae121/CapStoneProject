from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    daily_notes = models.TextField(blank=True, null=True)
    weekly_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Goal(models.Model):
    user = models.ForeignKey(User, related_name="goals", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
