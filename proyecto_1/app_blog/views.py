from datetime import date, datetime
from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from datetime import datetime


from app_blog.models import Post, Userpost, Ranking
from app_blog.form import User_form, Post_form, RankingForm

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
    

def post_form(request):
    if request.method == 'POST':
        post_form = Post_form(request.POST)
        if post_form.is_valid():
            data = post_form.cleaned_data
            post = Post(
                title=data['title'],
                author=data['author'],
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

def search(request):   
	if request.GET['all-search']:
		search_param = request.GET['all-search']
		#posts = Post.objects.filter(title__contains=search_param)
		query = Q(title__contains=search_param)
		query.add(Q(author__contains=search_param), Q.OR)
		posts = Post.objects.filter(query)

		context_dict = {
			'posts': posts
	    }

	return render(
		request=request,
		context=context_dict,
		template_name='app_blog/search.html',
	)

def buscarDatos(request):
	
	return render(request, "app_blog/search.html")