from django import forms
from .models import Tasks
from django_quill.forms import QuillFormField

class QuilEditor(forms.Form):
    comment = QuillFormField()


class TasksForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields="__all__"
