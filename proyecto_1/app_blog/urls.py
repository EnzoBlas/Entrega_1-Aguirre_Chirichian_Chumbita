from app_blog import views
from django.urls import path
from django.contrib import admin

app_name ='app_blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("posts/", views.posts, name="posts"),
    path("user-form/", views.user_forms, name="user-form"),
    path("post-form", views.post_form, name="post_form"),
    path('ranking/', views.ranking, name='ranking'),
    path('ranking-form/', views.ranking_form, name='ranking_form'),
    path('ranking-list/', views.ranking_list, name='ranking_list'),
    path('search_post/', views.search_post, name='search_post'),
    path('search/', views.search),

]