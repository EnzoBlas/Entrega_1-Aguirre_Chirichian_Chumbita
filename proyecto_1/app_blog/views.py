<<<<<<< HEAD
from turtle import title
=======
from xml.etree.ElementTree import Comment
>>>>>>> 4a150a42bf63ccd683065090d1b5758916a7377a
from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict

<<<<<<< HEAD
from app_blog.models import Post,Userpost
from app_blog.form import User_form,Post_form
=======
from app_blog.models import Comentario
from app_blog.form import ComentarioForm
>>>>>>> 4a150a42bf63ccd683065090d1b5758916a7377a

def index(request):
    return render(request, 'app_blog/home.html')

<<<<<<< HEAD
def posts(request):
    posts = Post.objects.all()

    context_dict = {
        'posts': posts
=======
def comments(request):
    comments = Comentario.objets.all()

    context_dict = {
        'comments': comments
>>>>>>> 4a150a42bf63ccd683065090d1b5758916a7377a
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/home.html",
    )


<<<<<<< HEAD
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
=======
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
>>>>>>> 4a150a42bf63ccd683065090d1b5758916a7377a
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/home.html"
            )

<<<<<<< HEAD
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
                due_date=data['due_date']
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
=======
    coment_form = ComentarioForm(request.POST)
    context_dict = {
        'coment_form': coment_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/coment_form.html'
    )
>>>>>>> 4a150a42bf63ccd683065090d1b5758916a7377a
