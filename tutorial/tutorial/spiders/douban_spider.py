#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = [
        "https://movie.douban.com/top250",
        "https://book.douban.com/top250"
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
