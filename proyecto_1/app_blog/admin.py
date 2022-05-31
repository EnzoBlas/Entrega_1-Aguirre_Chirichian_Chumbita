from django.contrib import admin
from .models import Post, Userpost
from .models import Ranking

# Register your models here.


admin.site.register(Post)
admin.site.register(Userpost)
admin.site.register(Ranking)
