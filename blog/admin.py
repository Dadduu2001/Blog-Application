from django.contrib import admin
from .models import Post

# Register your models here. Twter_lite = ab12cd34, Twter = Twter

class AdminPost(admin.ModelAdmin):
    list_display = ('author', 'title',)
    #for the searching of foreign key use this
    search_fields = ['title','author__username']

admin.site.register(Post, AdminPost)