# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import markdown
from django.shortcuts import render, get_object_or_404
from .models import Post, Categoty
from comments.forms import CommentForm
from django.http import HttpResponse


def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'blog/index.html', context={
                   'title': '我的博客首页' ,
                   'post_list': post_list
                })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    context = {'post': post,
               'form': form,
               'comment_list': comment_list
    }
    return render(request, 'blog/detail.html', context= context)


def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    ).order_by('-create_time')

    return  render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Categoty, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})