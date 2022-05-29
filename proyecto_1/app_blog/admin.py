from django.contrib import admin
from .models import Comentario

# Register your models here.


class postAdmin(admin.ModelAdmin):
    fields: ('title','slug','author','created_date','content')

    prepopulated_fields = {'slug':('title',)}

admin.site.register(Comentario,postAdmin)