from app_blog import views
from django.urls import path
from django.contrib import admin

app_name ='app_blog'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("comentform/", views.comentario_form, name="comentform"),
    path('ranking/', views.ranking, name='Ranking'),
    path('ranking-form/', views.ranking_form, name='RankingForm'),

]