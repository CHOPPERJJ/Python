#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 自己写的类、函数等的实现方式


import requests
from bs4 import BeautifulSoup


# # 1.用实体类的方式实现
# class Spider(object):
#
#     def __init__(self):
#         self.url = 'https://movie.douban.com/top250'
#
#     def parse(self, url):
#         r = requests.get(url)
#         soup = BeautifulSoup(r.content, 'html.parser')
#
#         movies = soup.find_all('div', class_='item')
#         for movie in movies:
#             title = movie.find('span', class_='title')
#             print(title)
#
#     # 启动函数，调用类里的函数必须要用实例self自己调用，不能直接调用
#     def start(self):
#         self.parse(self.url)
#
#
# # 主函数只能调用Spider()实体类，
# if __name__ == '__main__':
#     Spider().start()





# # 2.用实体类的方式实现
# class Spider(object):
#
#     def __init__(self):
#         self.url = 'https://movie.douban.com/top250'
#
#     def parse(self, url):
#         r = requests.get(url)
#         soup = BeautifulSoup(r.content, 'html.parser')
#
#         movies = soup.find_all('div', class_='item')
#         for movie in movies:
#             title = movie.find('span', class_='title')
#             print(title)
#
#     def start(self):
#         self.parse(self.url)
#
#
# if __name__ == '__main__':
#     shili = Spider()
#     shili.start()



# 3.用实体类的方式实现
class Spider(object):

    def __init__(self):
        self.url = 'https://movie.douban.com/top250'

    def parse(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        url1 = soup.find('div', class_='hd').a['href']
        url2 = soup.find('span', class_='next').a['href']
        url3 = self.url + url2
        print(url1)
        print(url2)
        print(url3)
        # for movie in movies:
        #     title = movie.find('span', class_='title')
        #     print(title)


if __name__ == '__main__':
    Spider().parse('https://movie.douban.com/top250')
