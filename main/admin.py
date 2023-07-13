from django.contrib import admin
from .models import (Tasks, CommentTasks, AnswerTasks)
# Register your models here.

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    ordering = ("order_num", )
    search_fields = ("title", )
    list_editable = ("order_num", )
    list_display_links = ("title", )
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("teacher", "add_time", "complite", "active")
    list_display = ("id", "title", "order_num", "teacher", "student", "complite", "active", "add_time", "complite_time")

    
@admin.register(CommentTasks)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "to", "comment", "add_time")

@admin.register(AnswerTasks)
class AnswerTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "teacher", "task", "checked", "add_time")