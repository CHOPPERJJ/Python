#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 匹配Regex对象
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found :' + mo.group() + ' ,' + mo.group(1) + ',' + mo.group(2))

# 利用括号分组
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found :' + mo.group(1))

# 用管道匹配多个分组
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo1.group())
print(mo2.group())

heroRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1 = heroRegex.search('Batmobile lost a wheel')
print(mo1.group())
print(mo1.group(1))

# 用问号实现可选匹配
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
mo2 = batRegex.search('The adventures of Batwoman')
print(mo1.group())
print(mo2.group())

# 建立自己的字符分类
vowelRegex = re.compile(r'[aeiouAEIOU]')
my = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(my)