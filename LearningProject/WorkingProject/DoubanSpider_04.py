#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 通过生成器优化代码

import requests
from bs4 import BeautifulSoup
import json

def start_requests(url):
    r = requests.get(url)
    return r.content


def parse(text):
    soup = BeautifulSoup(text, 'html.parser')
    movie_list = soup.find('div', class_ = 'item')
    for movie in movie_list:
        mydict = {}
        mydict['title'] = movie.find('span', class_ = 'title').text
        mydict['score'] = movie.find('span', class_ = 'rating_num').text
        quote = movie.find('span', class_ = 'inq')
        mydict['quote'] = quote.text if quote else None
        star = movie.find('div', class_ = 'inq')
        mydict['comment_num'] = star.find_all('span')[-1].text[:-1]
        yield mydict

def get_all():
    for i in range(2):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        text = start_requests(url)
        result = parse(text)
        yield from result
        