#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 多页抓取和二级页面抓取解析

import requests
from bs4 import BeautifulSoup
import json


def start_request(url):
    r = requests.get(url)
    return r.content


# 解析一级页面
def get_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    movies = soup.find_all('div', class_ = 'info')
    pages = []
    for movie in movies:
        url = movie.find('div', class_ = 'hd').a['href']
        pages.append(url)
    return pages

# 解析二级页面
def parser_page(text):
    soup = BeautifulSoup(text, 'html.parser')
    mydict = {}
    mydict['title'] = soup.find('span', property = 'v:itemreviewed').text
    mydict['duration'] = soup.find('span', property = 'v:runtime').text
    mydict['time'] = soup.find('span', property = 'v:initialReleaseDate').text
    return mydict


# 数据存储到json中
def write_json(result):
    s = json.dumps(result, indent=4, ensure_ascii=False)
    with open('movies.json', 'w', encoding='utf-8')as f:
        f.write(s)


def main():
    for i in range(7, 9):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        text = start_request(url)
        # 解析一级页面
        pageurls = get_page(text)
        for pageurl in pageurls: # 解析二级页面,pageurls为字典，包含了所有获取的二级页面的url地址，遍历pageurls获得单个pagerul
            get_second_page = start_request(pageurl) # 将单个的二级url传入函数start_request()进行数据获取
            second_mydict = parser_page(get_second_page) # 将单个解析后的值传入parser_page函数进行二级页面解析
            result_list.append(second_mydict)
            print(second_mydict)
    write_json(result_list)


if __name__ == '__main__':
    result_list = []
    main()
