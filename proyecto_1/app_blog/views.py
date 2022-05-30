from datetime import datetime
from turtle import title
from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

from app_blog.models import Post,Userpost
from app_blog.form import User_form,Post_form

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

            userposts = Userpost.objects.all()
            context_dict = {
                'userposts': userposts
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/home.html"
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
            post = Post(
                title=data['title'],
                author=data['author'],
                text=data['text'],
                due_date=data["due_date"],
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
