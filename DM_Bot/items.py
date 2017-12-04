# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmBotItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    EAN = scrapy.Field()
    IMG = scrapy.Field()
    Price = scrapy.Field()

