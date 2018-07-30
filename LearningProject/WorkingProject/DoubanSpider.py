#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import pprint


# 发送请求，获得网页的源代码
def startRequest(url):
    r = requests.get(url)
    return r.content


# 接收网页源代码解析出需要的数据格式
def parseUrl(text):
    soup = BeautifulSoup(text, 'html.parser')
    moveList = soup.find_all('div', class_='item')
    resultList = []
    for movie in moveList:
        mydict = {}
        mydict['title'] = movie.find('span', class_='title').text
        mydict['score'] = movie.find('span', class_='rating_num').text
        mydict['quote'] = movie.find('span', class_='inq').text
        star = movie.find('div', class_='star')
        mydict['commentNum'] = star.find_all('span')[3].text[:-3]
        resultList.append(mydict)
    return resultList


# 将解析的数据写入json
def writeJson(result):
    s = json.dumps(result, indent=4, ensure_ascii=False)
    with open('movies.json', 'w', encoding='utf-8') as f:
        f.write(s)


# 主函数,调用其他函数
def main():
    url = 'https://movie.douban.com/top250'
    text = startRequest(url)
    result = parseUrl(text)
    writeJson(result)


# 一般做法
if __name__ == '__main__':
    main()

