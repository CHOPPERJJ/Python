#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json

def start_requests(url):
    r = requests.get(url)
    return r.content


def parse(text):
    soup = BeautifulSoup(text, 'html.parser')
    movie_list = soup.find_all('div', class_='item')
    for movie in movie_list:
        mydict = {}
        mydict['title'] = movie.find('span', class_='title').text
        mydict['score'] = movie.find('span', class_='rating_num').text
        quote = movie.find('span', class_='inq')
        # 抓取10页就总会遇到这样的特殊情况
        mydict['quote'] = quote.text if quote else None
        star = movie.find('div', class_='star')
        mydict['comment_num'] = star.find_all('span')[-1].text[:-3]
        result_list.append(mydict)


def write_json(result):
    s = json.dumps(result, indent=4, ensure_ascii=False)
    with open('movies.json', 'w', encoding='utf-8') as f:
        f.write(s)


def main():
    for i in range(10):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        text = start_requests(url)
        parse(text)
    write_json(result_list)

if __name__ == '__main()__':
    result_list = []
    main()
