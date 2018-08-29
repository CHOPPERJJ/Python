#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# WSGI Web Server Gateway Interface
# hello.py


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


def app(environ, start_response):
    start_response('100 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello %s!</h1>' % (environ['PATH_INFO'][1:] or 'take')
    return [body.encode('utf-8')]

