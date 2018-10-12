#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import markdown

from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost
from django.shortcuts import render, redirect
# from .forms import ArticlePostForm
# from django.contrib.auth.models import User


# 主页视图
def article_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)


# 次级视图
def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
        extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
         ])

    context = {'article': article}
    return render(request, 'article/detail.html', context)


# 文章的视图
# def article_create(request):
#     if request.method == "POST":
#         article_post_form = ArticlePostForm(data=request.POST)
#         if article_post_form.is_valid():
#             new_article = article_post_form.save(commit=False)
#             new_article.author = User.objects.get(id=1)
#             new_article.save()
#             return redirect("article:article_list")
#         else:
#             return HttpResponse("表单内容错误，请重新填写。")
#     else:
#         article_post_form = ArticlePostForm()
#         context = { 'article_post_form': article_post_form }
#         return render(request, 'article/create.html', context)
