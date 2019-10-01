# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeathercrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    city = scrapy.Field()
    weather = scrapy.Field()
    maxTemperature = scrapy.Field()
    minTemperature = scrapy.Field()
    notice = scrapy.Field()
    pop = scrapy.Field()
    date = scrapy.Field()
    created_at = scrapy.Field()
    created_datetime = scrapy.Field()
    pass
