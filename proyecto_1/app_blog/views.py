from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

from app_blog.models import Post,Userpost
from app_blog.form import User_form,Post_form
from app_blog.models import Ranking
from app_blog.form import  RankingForm

def index(request):
    posts = Post.objects.all()

    context_dict = {
        'posts': posts
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/home.html",
    )

    
def posts(request):
    posts = Post.objects.all()

    context_dict = {
        'posts': posts
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/home.html",
    )


def user_forms(request):
    if request.method == 'POST':
        user_from = User_form(request.POST)
        if user_from.is_valid():
            data = user_from.cleaned_data
            userpost = Userpost(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
            )
            userpost.save()
            context_dict = {
                'userpost': userpost
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/userpk.html"
            )

    user_from = User_form(request.POST)
    context_dict = {
        'user_form': user_from
     }
    return render(
        request=request,
        context=context_dict,
        template_name='app_blog/user_form.html'
    )

def post_form(request):
    if request.method == 'POST':
        post_form = Post_form(request.POST)
        if post_form.is_valid():
            data = post_form.cleaned_data
            author=data['author']
            userpost = Userpost.objects.filter(author__contains=author)
            post = Post(
                title=data['title'],
                author=userpost['name'],
                text=data['text'],
            )
            post.save()

            posts = Post.objects.all()
            context_dict = {
                'posts': posts
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/home.html"
            )

    post_form = Post_form(request.POST)
    context_dict = {
        'post_form': post_form
     }
    return render(
        request=request,
        context=context_dict,
        template_name='app_blog/post_form.html'
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