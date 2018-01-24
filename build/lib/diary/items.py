# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DiaryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dlink=scrapy.Field()
    title=scrapy.Field()
    plink=scrapy.Field()
    time=scrapy.Field()
    views=scrapy.Field()
    comments=scrapy.Field()
    favor=scrapy.Field()
