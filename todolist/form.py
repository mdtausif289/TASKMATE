from django import forms
from .models import taskmate

class TaskForm(forms.ModelForm):
    class Meta:
        model = taskmate
        fields = ['addtask','done']