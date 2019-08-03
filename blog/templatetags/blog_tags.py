# coding:utf-8
from ..models import Post, Categoty
from django import template


# 自定义模板标签
register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


@register.simple_tag                  # 归档模板标签
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')            # DESC表示时间降序排列


@register.simple_tag
def get_categories():
    return Categoty.objects.all()