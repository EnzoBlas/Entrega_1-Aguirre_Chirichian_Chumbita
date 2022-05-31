from django import forms
from django.forms import ModelForm
from app_blog.models import Ranking

from app_blog.models import Userpost

class User_form(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

class Ranking_form(forms.Form):
    name_course = forms.CharField(max_length=40) 
    opinion = forms.CharField()
    score = forms.IntegerField(min_value=1, max_value=10)
    id_number = forms.IntegerField()

class Post_form(forms.Form):
    title = forms.CharField(max_length=40) 
    text = forms.CharField()
    id_number = forms.IntegerField()