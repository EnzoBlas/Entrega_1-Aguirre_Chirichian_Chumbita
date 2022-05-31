from django import forms
from django.forms import ModelForm
from app_blog.models import Comentario, Ranking

class ComentarioForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.CharField(max_length=30)
    content = forms.TextInput()

class RankingForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = ('name_course', 'opinion', 'score')

        
    


