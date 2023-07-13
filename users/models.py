from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    teacher = models.BooleanField(default=False)
    student = models.BooleanField(default=True)
    