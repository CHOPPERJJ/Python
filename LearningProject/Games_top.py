#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re

r = requests.get('http://www.ign.xn--fiqs8s/article/review')
soup = BeautifulSoup(r.content, 'html.parser')
game_list = soup.find_all('li', class_='tr')

for game in game_list:
    title = game.find('a').text
    score = game.find('span').text
    pannel = game.find('b').text
    comment = game.find('span', class_='info').text
    print(title, score, '\n', pannel, comment, '\n')