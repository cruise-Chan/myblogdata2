# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Categoty, Tag


# 定制Admin
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time', 'modified_time', 'category', 'author']

# 把新增的 PostAdmin也注册进来
admin.site.register(Post)
admin.site.register(Categoty)
admin.site.register(Tag)