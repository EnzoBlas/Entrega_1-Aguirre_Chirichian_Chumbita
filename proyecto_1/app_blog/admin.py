from django.contrib import admin
from .models import Comentario, Ranking
from .models import Post, Userpost

# Register your models here.

admin.site.register(Ranking)
admin.site.register(Post)
admin.site.register(Userpost)
