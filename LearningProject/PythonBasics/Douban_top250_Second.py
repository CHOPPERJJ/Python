#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 我们抓取标题、上映时间、电影时长三个指标。
# 代码逻辑是，抓取每个电影的链接，再对每个链接进行请求，解析每个电影详情页获取数据

import requests
from bs4 import BeautifulSoup
import json


def start_requests(url):
    print(url)
    r = requests.get(url)
    return r.content


# 解析一级网页，获取url列表
def get_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    movies = soup.find_all('div', class_='info')
    pages = []
    for movie in movies:
        url = movie.find('div', class_='hd').a['href']
        pages.append(url)
    return pages


# 解析二级网页，获取信息：
def parse_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    movies = soup.find_all('div', class_='info')
    mydict = {}
    mydict['title'] = soup.find('span', property='v:itemreviewed').text
    mydict['duration'] = soup.find('span', property='v:runtime').text
    mydict['time'] = soup.find('span', property='v:initialReleaseDate').text
    return mydict


# 将数据读取到json文件中：
def write_json(result):
    s = json.dumps(result, indent=4, ensure_ascii=False)
    with open('movies.json', 'w', encoding='utf-8') as f:
        f.write(s)


def main():
    for i in range(7, 9):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        text = start_requests(url)
        # 解析一级页面
        pageurls = get_page(text)
        # 解析二级页面
        for pageurl in pageurls:
            page = start_requests(pageurl)
            mydict = parse_page(page)
            result_list.append(mydict)
    write_json(result_list)


if __name__ == '__main__':
    result_list = []
    main()
