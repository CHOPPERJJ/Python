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
        for movie in movies:
            url = movie.find('div', class_='hd').a['href']
            self.qurl.put(url)

        nextpage = soup.find('span', class_='next').a['href']
        if nextpage:
            nexturl = self.start_url + nextpage
            self.parse_first(nexturl)
        else:
            self.first_running = False

    def parse_second(self):
        while self.first_running or not self.qurl.empty():
            url = self.qurl.get()
            print('crawling', url)
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'lxml')
            mydict = {}
            title = soup.find('div', property = 'v:itemreviewed')
            mydict['title'] = title.text if title else None
            duration = soup.find('span', property = 'v:runtime')
            mydict['duration'] = duration.text if duration else None
            time = soup.find('span', property = 'v:initialReleaseDate')
            mydict['time'] = time.text if time else None
            self.data.append(mydict)

@run_time
def run(self):
    ths = []