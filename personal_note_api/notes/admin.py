from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Goal

# Extend the default UserAdmin to include custom fields
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('daily_notes', 'weekly_summary')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('daily_notes', 'weekly_summary')}),
    )

    list_display = (
        'username',
        'email',
        'daily_notes',
        'weekly_summary',
        'is_staff',
        'is_active',
    )
    search_fields = ('username', 'email')


# Customize Goal admin
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)
