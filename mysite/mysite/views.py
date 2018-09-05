# -*- coding: utf-8 -*-

from django.http import HttpRequest


def first_page(request):
    return HttpRequest('hello world')