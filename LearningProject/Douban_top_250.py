#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import pprint
from bs4 import BeautifulSoup

r = requests.get('https://movie.douban.com/top250')
soup = BeautifulSoup(r.content, 'html.parser')
movie_list = soup.find_all('div', class_='item')
result_list = []

for movie in movie_list:
    mydict = {}
    mydict['title'] = movie.find('span', class_='title').text
    mydict['score'] = movie.find('span', class_='rating_num').text
    mydict['quote'] = movie.find('span', class_='inq').text

    star = movie.find('div', class_='star')
    mydict['comment_num'] = star.find_all('span')[-1].text[:-3]

    result_list.append(mydict)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(result_list)
