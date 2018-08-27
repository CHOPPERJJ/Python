#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 通过生成器优化代码

import requests
from bs4 import BeautifulSoup
import json


def start_requests(url):
    r = requests.get(url)
    return r.content


class Doubantop(object):

    def __init__(self):
        self.baseurl = 'https://movie.douban.com/top250'
        self.result_list = []

    def start_request(self, url):
        r = requests.get(url)
        return r.content

    def parser(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        movie_list = soup.find_all('div', class_ = 'item')
        for movie in movie_list:
            mydict = {}
            mydict['title'] = movie.find('span', class_ = 'title').text
            mydict['score'] = movie.find('span', class_ = 'rating_num').text
            quote = movie.find('span', class_ = 'inq')
            mydict['quote'] = quote.text if quote else None
            star = movie.find('div', class_='star')
            mydict['comment_num'] = star.find_all('span')[-1].text[:-3]
            self.result_list.append(mydict)
        nextpage = soup.find('span', class_ = 'next').a
        if nextpage:
            nexturl = self.baseurl + nextpage['href']
            text = self.start_request(nexturl)
            self.parser(text)

    def write_json(self, result):
        s = json.dumps(result, indent=4, ensure_ascii = False)
        with open('movie.json', 'w', encoding = 'utf-8') as f:
            f.write(s)

    def start(self):
        text = self.start_request(self.baseurl)
        self.parser(text)
        self.write_json(self.result_list)


douban = Doubantop()
douban.start()
