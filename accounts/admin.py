from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages

from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.action(description="Make selected users superusers")
def make_superuser(modeladmin, request, queryset):
    queryset.update(is_superuser=True, is_staff=True)
    messages.success(request, f"{queryset.count()} user(s) were successfully made superusers.")

@admin.action(description="Remove superuser status")
def remove_superuser(modeladmin, request, queryset):
    queryset.update(is_superuser=False)
    messages.success(request, f"Superuser status removed from {queryset.count()} user(s).")

@admin.action(description="Activate selected users")
def activate_users(modeladmin, request, queryset):
    queryset.update(is_active=True)
    messages.success(request, f"{queryset.count()} user(s) were successfully activated.")

@admin.action(description="Deactivate selected users")
def deactivate_users(modeladmin, request, queryset):
    queryset.update(is_active=False)
    messages.success(request, f"{queryset.count()} user(s) were successfully deactivated.")


User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    actions = [make_superuser, remove_superuser, activate_users, deactivate_users] + list(UserAdmin.actions)
    list_display = [ 'id', 'username', 'email', 'is_superuser', 'is_active', 'last_login']
    list_filter = list(UserAdmin.list_filter) + ['is_superuser', 'is_active']


admin.site.register(User, CustomUserAdmin)
