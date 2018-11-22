# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThinkTankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 标签
    tag = scrapy.Field()
    # 数据
    data = scrapy.Field()
    # 网站名
    site = scrapy.Field()
