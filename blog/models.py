# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django.utils.six import python_2_unicode_compatible     python2需要这句


class Categoty(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)     # 文章摘要
    category = models.ForeignKey(Categoty)                     # 课程名称
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})


    class Meta:
        ordering = ['-create_time']