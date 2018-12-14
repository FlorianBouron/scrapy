# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


def shorten_amazon_link(link):
	product_id = link.split('/')[-1]
	return 'https://amazon.fr/dp/' + product_id

class ProductItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()

class ProductItemLoader(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field(input_processor = MapCompose(shorten_amazon_link))