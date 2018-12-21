#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# # 自定义模型管理器
# class ArticleManager(models.Manager):
#     def get_queryset(self):
#         return super(ArticleManager, self).get_queryset().filter(status='Article')


# 博客文章数据模型
class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    # objects = models.Manager()    #默认的管理器
    # Articled = ArticleManager()    #自定义管理器

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


