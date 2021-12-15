from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, BlogCategory

class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ('slug',)
    list_display = ('id', 'title', 'category', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 25
    summernote_fields = ('content',)


class BlogCategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('id', 'category', 'slug', 'date_created')
    list_display_links = ('id', 'category')
    search_fields = ('category',)
    list_per_page = 25

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)

