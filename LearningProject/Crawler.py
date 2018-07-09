#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


from bs4 import BeautifulSoup
# 传入URL
r = requests.get('https://www.csdn.net/')

# 解析URL
soup = BeautifulSoup(r.text, 'html.parser')
content_list = soup.find_all('div', attrs={'class': 'title'})
comment_count = soup.find_all('dl', attrs={'class': 'list_userbar'})

for content in content_list:
    print(content.h2.a.text)
