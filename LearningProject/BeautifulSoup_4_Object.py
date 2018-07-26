#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'lxml')
tag = soup.b
type(tag)

# 修改tag属性
tag['class'] = 'verybold'
tag['id'] = 'littlebold'
del tag['id']

print(tag)
print(tag['class'])
print(tag.attrs)
print(tag.get_text())
print(tag.get('class'))
print(tag.get('id'))

# 多值属性
# 一个tag可以有多个CSS的class
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
print(css_soup.p['class'])

# 将tag转换成字符串时,多值属性会合并为一个值
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'lxml')
print(rel_soup.a['rel'])
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)