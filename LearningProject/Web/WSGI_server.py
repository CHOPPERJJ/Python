#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# WSGI Web Server Gateway Interface
# server.py

from wsgiref.simple_server import make_server
from WSGI import app

# 创建服务器，IP地址为空，端口为8000
httpd = make_server('', 8000, app)
print('Server HTTP on port 8000...')
# 开始监听HTTP的请求
httpd.serve_forever()

