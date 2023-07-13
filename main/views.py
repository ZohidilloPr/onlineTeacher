from datetime import datetime
from django.utils import timezone
from .forms import QuilEditor, TasksForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from .models import (Tasks, CommentTasks, AnswerTasks)

# Create your views here

today = timezone.now().day
User = get_user_model()

def TasksList(request):
    """ BUGINGI VAZIFALARNI KO'RISH UCHUN """
    if request.user.is_superuser:
        tasks = Tasks.objects.filter(active=True, add_time__day=today).all()
    elif request.user.teacher:
        tasks = Tasks.objects.filter(active=True, add_time__day=today, teacher=request.user).all()
    elif request.user.student:
        tasks = Tasks.objects.filter(active=True, add_time__day=today, student=request.user).all()
    else:
        tasks = []
    return render(request, "users/pages/tasks.html", {"tasks": tasks})


def WriteComment(request):
    """ VAZIFALARGA IZOH QOLDIRISH """
    if request.method == "POST":
        try:
            user = User.objects.get(id=int(request.POST.get("author")))
            to = User.objects.get(id=int(request.POST.get("to")))
            task = Tasks.objects.get(id=int(request.POST.get("task")))
            comment = request.POST["comments"]
            comments = CommentTasks.objects.create(
                author=user,
                to=to,
                task=task,
                comment=comment,
            ) 
            comments.save()
            return redirect("tasks_today")
        except Exception as e:
            print(e)
    return render(request, "forms/comment_form.html")


def NoComplitedTasks(request):
    """ TUGALLANMAGAN VAZIFALAR """
    tasks = Tasks.objects.filter(complite=False, student=request.user).order_by("-add_time")
    return render(request, "users/pages/no_compited_tasks.html", {"tasks": tasks})


def AnswerSend(request, id):
    """ VAZIFA YUKLASH UCHUN """
    task = Tasks.objects.get(id=id)
    if request.method == "POST":
        try:
            teacher = User.objects.get(id=task.teacher.id)
            student = User.objects.get(id=task.student.id)
            file = request.POST["file"]
            comment = request.POST["comment"]
            answer = AnswerTasks.objects.create(
                student=student,
                teacher=teacher,
                task=task, comment=comment, file=file
            )
            answer.save()
        except Exception as e:
            print(e)
    return render(request, "forms/answer_form.html", {"form": QuilEditor(), "task": task})


def AddTasks(request):
    """ VAZIFALARNI QO'SHISH """
    if request.method == "POST":
        try:
            if request.POST["student"].isdigit():
                teacher = User.objects.get(id=request.user.id)
                student = User.objects.get(id=int(request.POST["student"]))
                title = request.POST['title']
                description = request.POST['comment']
                order_num = request.POST["order_num"]
                add_time = timezone.make_aware(datetime.strptime(request.POST['add_time'], '%Y-%m-%dT%H:%M'))
                complite_time = timezone.make_aware(datetime.strptime(request.POST['complite_time'], '%Y-%m-%dT%H:%M'))
                slug = request.POST['slug'] 
                task = Tasks.objects.create(
                    teacher=teacher,
                    student=student, 
                    title=title, 
                    description=description,
                    order_num=order_num,
                    add_time=add_time,
                    complite_time=complite_time,
                    slug=slug
                )
                task.save()
                return redirect("add_task")
        except Exception as e:
            print(e)
        
    return render(request, "forms/add_tasks.html", {
        "form": QuilEditor(), 
        "students": User.objects.filter(student=True)}
    )
    
