from django.contrib import admin
from .models import Post, Userpost

# Register your models here.


class postAdmin(admin.ModelAdmin):
    fields: ('title','slug','author','created_date','content')

    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post)
admin.site.register(Userpost)