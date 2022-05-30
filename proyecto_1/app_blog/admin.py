from django.contrib import admin
from .models import Comentario, Ranking

# Register your models here.


#class postAdmin(admin.ModelAdmin):
 #   fields: ('title','slug','author','created_date','content')

  #  prepopulated_fields = {'slug':('title',)}

admin.site.register(Comentario) #(Comentario, PostAdmin)
admin.site.register(Ranking)