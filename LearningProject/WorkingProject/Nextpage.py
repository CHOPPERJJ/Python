#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


# class Spider(object):
#     def __init__(self):
#         self.url = 'https://movie.douban.com/top250'

    # def parse(self):
r = requests.get('https://movie.douban.com/top250')
soup = BeautifulSoup(r.content, 'html.parser')

movies = soup.find_all('div', class_='item')
for movie in movies:
    title = movie.find('span', class_ = 'title').text
    print(title)

# if __name__ == '__main__':
#     Spider().parse()
