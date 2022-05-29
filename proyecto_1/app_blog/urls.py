from app_blog import views
from django.urls import path

app_name ='app_blog'
urlpatterns = [
    path("", views.index, name='home'),

]