#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms
from .models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'body')
