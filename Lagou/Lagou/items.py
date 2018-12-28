# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class LagouItem(Item):
    title = Field()
    location = Field()
    salary = Field()
    company = Field()
    fintance = Field()
