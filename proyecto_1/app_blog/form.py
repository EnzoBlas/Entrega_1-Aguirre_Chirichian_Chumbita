from cgitb import text
import datetime
from datetime import date, datetime
from django import forms
from django.forms import ModelForm

from app_blog.models import Userpost

class User_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

class Post_form(forms.Form):
    title = forms.CharField(max_length=40)
    author = forms.IntegerField() 
    text = forms.CharField()
    due_date = forms.DateField()
