import datetime
from datetime import date, datetime
from django import forms
from django.forms import ModelForm
from app_blog.models import Comentario

class ComentarioForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.CharField(max_length=30)
    content = forms.TextInput()


