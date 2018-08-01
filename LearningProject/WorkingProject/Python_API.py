#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python api

import requests
import operator
import json
import time


def start_request(url):
    print('Getting', url)
    r = requests.get(url, auth=('chopper_jj@qq.com', 'github3112152'))
    return r


def get_info(rep):
    datas = rep.json
    for data in datas:
        yield {
            'project_name': data['full_name'],
            'project_url': data['html_url'],
            'project_api_url': data['url'],
            'star_count': data['stargazers_count']
        }


def get_all():
    baseurl = 'https://api.github.com/repos/python/cpython/forks?page={}'
    for i in range(1, 171+1):
        url = baseurl.format(i)
        r = start_request(url)
        yield from get_info(r)


def main():
    start = time.time()
    datas =list(get_all())
    datas.sort(key=operator.itemgetter('star_count'), reverse = True)
    s = json.dump(datas, indent=4, ensure_ascii=False)
    with open('github.json', 'w', encoding='utf-8')as f:
        f.write(s)
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()
