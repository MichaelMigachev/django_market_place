from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'published', 'views')
    list_filter = ('published', 'created_date')
    search_fields = ('title', 'content')
