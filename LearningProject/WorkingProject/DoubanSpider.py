#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json


def startRequest(url):
    r = requests.get(url)
    return r


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
        mydict['commentNum'] = star.find_all('span')[-1].text[:-3]
        print(title, score, '\n', commentNum, '\n')
