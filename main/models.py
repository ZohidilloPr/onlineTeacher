from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Tasks(models.Model):
    """ VAZIFALAR UCHUN MODEL """
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="O'qituvchi", related_name="teachers")
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Talaba", related_name="students")
    title = models.CharField(max_length=500, verbose_name="Vazifa mavzusi")
    description = QuillField(verbose_name="Tafsiloti")
    complite = models.BooleanField(default=False, verbose_name="Bitdi")
    order_num = models.IntegerField(default=0, verbose_name="Tartib raqami")
    add_time = models.DateTimeField(default=timezone.now, blank=True, verbose_name="Vazifa berilayotgan vaqt")
    complite_time = models.DateTimeField(verbose_name="Vazifani topshirish vaqti")
    active = models.BooleanField(default=True)
    slug = models.SlugField(verbose_name="slug", max_length=300)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return str(self.title)
    
    def get_comments(self):
        total = self.commenttasks_set.all() 
        return total
    
    class Meta:
        db_table = ''
        managed = True
        ordering = ["order_num"]
        verbose_name = "Tasks"
        verbose_name_plural = "Tasks"


class CommentTasks(models.Model):
    """ VAZIFALAR UCHUN IZOHLAR """
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="comment_authors")
    to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="comment_tos")
    task = models.ForeignKey(Tasks, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(verbose_name="Izoh")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)

    def __unicode__(self):
        return str(self.author)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = "Izohlar"
        verbose_name_plural = "Izohlar"

class AnswerTasks(models.Model):
    """ JAVOBLARNI QOLDIRISH UCHUN """
    student = models.ForeignKey(User, related_name="answer_students", on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(User, related_name="task_teacher", on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey(Tasks, on_delete=models.SET_NULL, null=True)
    comment = QuillField()
    file = models.FileField(upload_to="file/answers/%Y-%m-%d/", blank=True, null=True)
    checked = models.BooleanField(default=False)
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} | {self.task}"

    def __unicode__(self):
        return str(self.student)
    
    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Javoblar"
        verbose_name_plural = "Javoblar"