#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost


def article_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)
