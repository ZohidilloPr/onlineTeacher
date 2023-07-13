from django.urls import path
from .views import (
    TasksList, 
    WriteComment,
    NoComplitedTasks, AnswerSend, AddTasks
)

urlpatterns = [
    # tasks
    path(
        "tasks/today/",
        TasksList,
        name="tasks_today"
    ),
    path(
        "tasks/no_complited/",
        NoComplitedTasks,
        name="no_complited_task"
    ),
    path(
        "tasks/add/",
        AddTasks,
        name="add_task"
    ),
    # comments
    path(
        "write/comment/",
        WriteComment,
        name="write_comment"
    ),
    # answers
    path(
        "send_answer/<int:id>/",
        AnswerSend,
        name="send_answer"
    ),
]
