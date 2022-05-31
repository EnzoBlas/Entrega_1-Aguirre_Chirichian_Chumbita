from app_blog import views
from django.urls import path
from django.contrib import admin

app_name ='app_blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path('ranking/', views.ranking, name='Ranking'),
    path('ranking-form/', views.ranking_form, name='RankingForm'),
    path("posts/", views.posts, name="posts"),
    path("user-form/", views.user_forms, name="user-form"),
    path("post-form", views.post_form, name="post_form"),
    path('search/', views.search),
    path('search-data/', views.buscarDatos, name='Search-Data'),
]