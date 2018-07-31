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
