from django.contrib import admin
from .models import Post
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'published_date', 'created_date', 'updated_at')
    ordering = ('-created_at',)
    list_filter = ('published_date',)
    search_fields = ('title', 'text')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, PostAdmin)
