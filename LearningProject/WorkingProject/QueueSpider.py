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
        print('running', end-start, 's')
    return wrapper


class Spider():

    def __init__(self):
        self.qurl = Queue() #url队列
        self.data = list()
        self.email = 'chopper_jj@qq.com'
        self.passward = 'github3112152'
        self.page_num = 171
        self.thread_num = 1000

# 生产所有url,存储到Queue队列qurl中
    def produce_url(self):
        baseurl = 'https://api.github.com/repos/python/cpython/forks?page={}' #github提供api地址
        for i in range(1, self.page_num + 1):
            url = baseurl.format(i)
            self.qurl.put(url) # 生成URL存入队列，等待其他线程提取

    def get_info(self):
        while not self.qurl.empty():  # 保证url遍历结束后退出线程，当线程队列不为空
            url = self.qurl.get()
            print('crawing', url)
            req = requests.get(url, auth = (self.email, self.passward))
            data = req.json()
            for datai in data:
                result = {
                    'project_name': datai['full_name'],
                    'project_url': datai['html_url'],
                    'project_api_url': datai['url'],
                    'star_count': datai['stargazers_url']
                }
                self.data.append(result)

    @run_time
    def run(self):
        self.produce_url()

        ths = []
        for _ in range(self.thread_num):
            th = Thread(target=self.get_info)
            th.start()
            ths.append(th)
        for th in ths:
            th.join()

        s = json.dumps(self.data, ensure_ascii=False, indent=4)
        with open('github_thread.json', 'w', encoding='utf-8') as f:
            f.write(s)

        print('Data crawling is finished')


if __name__ == '__main__':
    Spider().run()