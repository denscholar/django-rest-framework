from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'content', 'created']
    list_filter = ['created']

admin.site.register(Post, PostAdmin)

