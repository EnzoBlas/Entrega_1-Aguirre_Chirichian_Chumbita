from datetime import date, datetime
from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Q

from datetime import datetime

from app_blog.models import Post,Userpost,Ranking
from app_blog.form import User_form,Post_form,Ranking_form


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
                email=data['email']
            )

            userpost.save()

            context_dict = {
                'userpost': userpost,
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/created_user.html"
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
            data_author=(str(Userpost.objects.filter(pk__contains=data['id_number']))[22:-3])
            post = Post(
                title=data['title'],
                text=data['text'],
                author=data_author
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
    return render(
        request=request,
        template_name="app_blog/ranking.html"
    )

def ranking_list(request):
    rankings = Ranking.objects.all()

    context_dict = {
        'rankings': rankings
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/ranking_list.html"
    )

def ranking_form(request):
    if request.method == "POST":
        ranking_form = Ranking_form(request.POST)
        if ranking_form.is_valid():
            data = ranking_form.cleaned_data
            data_author=(str(Userpost.objects.filter(pk__contains=data['id_number']))[22:-3])
            ranking = Ranking(
                name_course=data["name_course"],
                opinion=data["opinion"],
                score=data["score"],
                author=data_author
                )
            ranking.save()

        rankings = Ranking.objects.all()
        context_dict = {
            'rankings': rankings
        }
        return render(
                request=request,
                context=context_dict,
                template_name="app_blog/ranking_list.html"
            )
    
    ranking_form = Ranking_form(request.POST)
    context_dict = {
        'ranking_form' : ranking_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_blog/ranking_form.html'
    )

def search(request):
    return render(request, "app_blog/search.html")

def search_post(request):
    context_dict = dict()
    if request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(title__contains=search_param)
        query.add(Q(text__contains=search_param), Q.OR)
        posts = Post.objects.filter(query)
        context_dict = {
            'posts': posts
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/search.html",
    )