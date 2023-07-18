from django.contrib import admin
from .models import CustomUser, StudentsGroup
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


@admin.register(StudentsGroup)
class StudentsGroupAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display_links = ["name"]
    filter_horizontal = ["students"]
    list_filter = ["teacher", "add_time"]
    list_display = ["id", "name", "teacher", "add_time", "update_time"]
