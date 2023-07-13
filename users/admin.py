from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display_links = ("username", )
    readonly_fields = ("date_joined", "last_login")
    list_display = ("id", "username", "last_login")

    fieldsets = (
        ("Personal Informatins", {
            "fields": (
                "first_name",
                "last_name",
                "username",
                "email",
                "password",
            ),
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                ("teacher",
                "student"),
                "groups",
                "user_permissions"
            ),
        }),        
        ("Time", {
            "fields": (
                "date_joined",
                "last_login",
            ),
        }),


    )