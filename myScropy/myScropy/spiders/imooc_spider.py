#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrapy


class ImoocSpider(scrapy.Spider):
    # spider的名字定义了Scrapy如何定位(并初始化)spider，所以其必须是唯一的
    name = 'imooc'

    # URL列表
    start_url = ['http://www.imooc.com/course/list']
    # 域名不在列表中的URL不会被爬取。
    allowed_domains = ['www.imooc.com']

    def parse(self, response):
        learn_nodes = response.css('a.course-card')
        for learn_node in learn_nodes:
            learn_url = learn_node.css('::attr(href)').extract_first()
            yield scrapy.Request(url=urlparse.urljoin(response.url, learn_url), callback=self.parse_learn)

    def parse_learn(self, response):
        title = response.xpath('//h2[@class="l"]/text()').extract_first()
        content = response.xpath('//div[@class="course-brief"]/p/text()').extract_first()
        url = response.url
        print('标题：' + title)
        print('地址：' + url )