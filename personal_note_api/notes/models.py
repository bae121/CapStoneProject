from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    daily_notes = models.TextField(blank=True, null=True, help_text="Optional daily notes for the user")
    weekly_summary = models.TextField(blank=True, null=True, help_text="Optional weekly summary for the user")

    def __str__(self):
        return self.username


class Goal(models.Model):
    user = models.ForeignKey(
        User,
        related_name="goals",
        on_delete=models.CASCADE,
        help_text="The user who owns this goal"
    )
    title = models.CharField(max_length=255, help_text="Title of the goal")
    description = models.TextField(blank=True, null=True, help_text="Detailed description of the goal")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def __str__(self):
        return f"{self.title} ({self.user.username})"
