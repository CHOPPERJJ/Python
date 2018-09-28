#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import ArticlePost

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)