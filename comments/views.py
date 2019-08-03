# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Comment

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # HTTP请求有get和post两种，一般用户通过表单提交数据都是通过post请求
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST中，这是一个类字典对象
        # 我们利用这些数据构造了 CommentForm 的实例， 这样Django的表单就生成了。
        form = CommentForm(request.POST)

        # 当调用 form.is_valid()方法时， Django自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # commit=False 的作用是仅仅利用表单的诗句生成 Comment模型类的实例，但还不保存评论数据到数据库
            comment = form.save(commit=False)

            # 将评论和评论的相关文章关联起来。
            comment.post = post

            # 最终将评论数据保存进数据库，调用模型实例的save方法。
            comment.save()

            # 重定向到 post 的详情页，实际上当 redirect 函数收到一个模型的实例时，他会调用这个模型实例的 get_absolute_url 方法。
            # 然后重定向到 get_absolute_url 方法返回的URL.

            return redirect(post)

        else:
            # Post.objects.filter(category=cate)也可以等价写成 cate.post_set.all()
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(post)