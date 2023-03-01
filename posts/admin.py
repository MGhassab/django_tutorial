# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post, Comment
class CommentAdmininline(admin.TabularInline):
    model = Comment
    fields = ['text']
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ['id', 'title', 'is_enable', 'publish_date', 'created_time']
    inlines = [CommentAdmininline, ]
    
    
#class CommentAdmin(admin.ModelAdmin):
#   list_display = ['post', 'text ', 'created_time']

#admin.site.register(Post, PostAdmin)
#admin.site.register(Comment, CommentAdmin)