#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 多线程爬虫实现2

import requests
import time
from threading import Thread
import json
from queue import Queue
from bs4 import BeautifulSoup


def run_time(func):
    def wrapper(*args, **kw):
        start = time.time()
        func(*args, **kw)
        end = time.time()
        print('running', end - start, 's')

    return wrapper


class Spider():
    def __init__(self):
        self.start_url = 'https://movie.douban.com/top250'
        self.qurl = Queue()
        self.data = list()
        self.item_num = 5
        self.thread_num = 10
        self.first_running = True

    def parse_first(self):
        print('crawling', url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')

        movies = soup.find_all('div', class_='info')[:self.item_num]
