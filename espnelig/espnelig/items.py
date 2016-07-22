# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EligibilityItem(scrapy.Item):
    pid = scrapy.Field()
    name = scrapy.Field()
    team = scrapy.Field()
    positions = scrapy.Field()
