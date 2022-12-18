from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'header_image', 'title_tag', 'author', 'post_date', 'category', 'snippet')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')
    list_filter = ('category', 'author')
    save_on_top = True



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('title',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'email')
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'date_added')
    list_filter = ('name',)



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
