from django.contrib import admin
from blog.models import Post 
# Register your models here.

class PostAdmin(admin.ModelAdmin): 
    list_d = ('title','modify_date')
    list_f = ('modify_date'),
    search_f = ('title','content')
    prepo_f = {'slug' : ('title',)}


admin.site.register(Post,PostAdmin)
