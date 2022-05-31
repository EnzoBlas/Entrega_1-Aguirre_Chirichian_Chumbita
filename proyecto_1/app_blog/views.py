from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.forms.models import model_to_dict
from datetime import datetime, timezone
from django.shortcuts import redirect

from app_blog.models import Comentario, Ranking
from app_blog.form import ComentarioForm, RankingForm

def index(request):
    return render(request, 'app_blog/home.html')

def comments(request):
    comments = Comentario.objets.all()

    context_dict = {
        'comments': comments
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/home.html",
    )


def comentario_form(request):
    if request.method == 'POST':
        coment_form = ComentarioForm(request.POST)
        if coment_form.is_valid():
            data = coment_form.cleaned_data
            coment = Comentario(title=data['title'], author=data['author'], content=data['content'])
            coment.save()

            comentario = Comentario.objects.all()
            context_dict = {
                'comentario': comentario
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/home.html"
            )

    coment_form = ComentarioForm(request.POST)
    context_dict = {
        'coment_form': coment_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/coment_form.html'
    )


def ranking(request):
    rankings = Ranking.objects.all()

    context_dict = {
        'rankings': rankings
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/ranking.html"
    )


def ranking_form(request):
    if request.method == "POST":
        ranking_form = RankingForm(request.POST)
        if ranking_form.is_valid():
            ranking = ranking_form.save(commit=False)
            #omitir esto
            #ranking.author = request.user
            #ranking.published_date = datetime.now()
            ranking.save()

        rankings = Ranking.objects.all()
        context_dict = {
            'rankings': rankings
        }
        return render(
                request=request,
                context=context_dict,
                template_name="app_blog/ranking.html"
            )

    ranking_form = RankingForm(request.POST)
    context_dict = {
        'ranking_form': ranking_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_blog/ranking_form.html'
    )

