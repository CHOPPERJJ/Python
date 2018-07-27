#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from bs4 import NavigableString
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# BeautifulSoup解析上面html_doc的HTML代码块
soup = BeautifulSoup(html_doc, 'html.parser')

# # 输出正常排序的HTML
# print(soup.prettify())
#
# # 文档中获取所有文字内容
# print(soup.get_text())
#
# # 找到<a>标签的连接
# for link in soup.find_all('a'):
#     print(link.get('href'))
# # <a>标签的文字内容
#     print(link.get_text())
#
# # 搜索文档树find_all()和find
# print(soup.find_all('b'))
# print(soup.b)
#
# # 正则表达式筛选
# for tag in soup.find_all(re.compile('^b')):
#     print(tag.name)
#
# print(soup.find_all(['a', 'b']))
#
# for tag in soup.find_all(True):
#     print(tag.name)

# # 如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 [4] ,如果这个方法返回 True
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
#
# print(soup.find_all(has_class_but_no_id))

# # find_all(name, attrs, recursive, string, **kwargs)方法搜索tag的所有子节点
# print(soup.find_all('title'))
# print(soup.find_all('p', 'title'))
# print(soup.find_all('a'))
#
# # 搜索所有id属性，值为link2
# print(soup.find_all(id = 'link2'))

# # 中查找所有包含 id 属性的tag,无论 id 的值是什么
# print(soup.find_all(id=True))
#
# # 多个指定名字的参数可以同时过滤tag的多个属性
# print(soup.find_all(href=re.compile('elsie'), id='link1'))
#
# # 按照CSS类名搜索tag,class_
# print(soup.find_all('a', class_='sister'))
# print(soup.find(class_=re.compile('itl')))

#
# def has_six_charactors(css_class):
#     return css_class is not None and len(css_class) == 6
#
#
# # class_字符串的长度为6
# print(soup.find_all(class_=has_six_charactors))

# # css值完全匹配,或者分别搜索每个类名匹配
# css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
# print(css_soup.find_all('p', class_='strikeout'))
# print(css_soup.find_all('p', class_='body'))
# print(css_soup.find_all('p', class_='body strikeout'))

# 通过 string 参数可以搜搜文档中的字符串内容
print(soup.find_all(string='Elsie'))
print(soup.find_all('a', string='Elsie'))
print(soup.find('a', class_='sister'))
print(soup.a.string)
print(soup.find_all(string=['Tillie', 'Elsie', 'Lacie']))
print(soup.find_all(string=re.compile('Dor')))

