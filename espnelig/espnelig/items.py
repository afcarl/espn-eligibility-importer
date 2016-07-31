# -*- coding: utf-8 -*-
import scrapy


class EligibilityItem(scrapy.Item):
    pid = scrapy.Field()
    name = scrapy.Field()
    team = scrapy.Field()
    primary_position = scrapy.Field()
    eligible_positions = scrapy.Field()
    all_positions = scrapy.Field()
