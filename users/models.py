from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

# User = get_user_model()

class CustomUser(AbstractUser):
    """ custom user for authentication """
    teacher = models.BooleanField(default=False)
    student = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    

class StudentsGroup(models.Model):
    """ student groups for dvide tasks """
    teacher = models.ForeignKey(CustomUser, related_name="group_teachers", on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250, verbose_name="Gurux nomi")
    students = models.ManyToManyField(CustomUser, related_name="group_students")
    add_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = _("StudentsGroup")
        verbose_name_plural = _("StudentsGroups")


    def __str__(self):
        return self.name


    def __unicode__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("StudentsGroup_detail", kwargs={"pk": self.pk})
