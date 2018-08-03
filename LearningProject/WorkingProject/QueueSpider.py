#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 多线程爬虫实现


import requests
import time
from threading import Thread
from queue import Queue
import json


def run_time(func):
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        end = time.time()
        print('running', end - start, 's')

    return wrapper()

class Spider():


    def __init__(self):
        self.qurl = Queue()
        self.data = list()
        self.email = 'chopper_jj@qq.com'
        self.passward = 'github3112152'
        self.page_num = 171
        self.thread_num = 10


    def
