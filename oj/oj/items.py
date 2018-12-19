# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OjItem(scrapy.Item):
    number = scrapy.Field()
    title = scrapy.Field()
    category = scrapy.Field()
    desc = scrapy.Field()
    input_desc = scrapy.Field()
    output_desc = scrapy.Field()
    example_input = scrapy.Field()
    example_output = scrapy.Field()
    tig = scrapy.Field()
