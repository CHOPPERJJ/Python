#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup


# 发送请求，获取网页源代码以供解析
def start_reqyests(url):
    r = requests.get(url)
    return r.content


# 接收网页源代码解析出需要的信息
def parse(text):
    soup = BeautifulSoup(text, 'html.parser')
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
    return result_list


# 将数据写入json
def write_json(result):
    s = json.dumps(result, indent=4, ensure_ascii=False)
    with open('movies.json', 'w', encoding='utf-8') as f:
        f.write(s)


# 主函数，调用其他函数
def main():
    url = 'https://movie.douban.com/top250'
    text = start_reqyests(url)
    result = parse(text)
    write_json(result)


if __name__ == '__main__':
    main()
