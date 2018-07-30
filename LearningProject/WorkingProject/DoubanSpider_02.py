#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json


def start_request(url):
    r = requests.get(url)
    return r.content


def parser_url(text):
    soup = BeautifulSoup(text, 'html.parser')
    movie_list = soup.find_all('div', class_ = 'item')
    result_list = []
    for movie in movie_list:
        mydict = {}
        mydict['title'] = movie.find('span', class_ = 'title').text
        mydict['score'] = movie.find('span', class_ = 'rating_num').text
        mydict['quote'] = movie.find('span', class_ = 'inq').text
        star = moive.find('div', class_ = 'star')
        mydict['comment_num'] = star.find_all('span')[-1].text[:-3]
        result_list.append(mydict)
    return result_list


def write_json(result):
    s = json.dumps(result, indent = 4, ensure_ascii = False)
    with open('movie.json', 'w', encoding = 'utf-8') as f:
        f.write(s)


def main():
    for i in range(10):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        text = start_request(url)
        result = parser_url(text)
        write_json(result)


if __name__ == '__main__'
    main()