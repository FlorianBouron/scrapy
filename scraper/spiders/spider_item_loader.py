import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst
from scraper.items import ProductItemLoader

def truncate_text(text):
	return text[:50]

class ProductDetails(scrapy.Spider):
	name = 'amazon_product_scraper_itemloader'
	start_urls = ['https://www.amazon.fr/s/ref=nb_sb_noss_2?'\
					'url=search-alias%3Daps&field-keywords=macbook']

	def parse(self, reponse):
		search_results = reponse.css('ul.s-result-list > li')
		for product in search_results:
			product_loader = ItemLoader(item = ProductItemLoader(), selector = product)
			product_loader.default_input_processor = MapCompose(truncate_text)
			product_loader.default_output_processor = TakeFirst()
			product_loader.add_css('title', '.s-access-title::text')
			product_loader.add_css('link', 'a.s-access-detail-page::attr(href)')
			product_loader.add_css('price', '.s-price::text')

			yield product_loader.load_item()