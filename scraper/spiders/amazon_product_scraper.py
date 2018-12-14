import scrapy
from scraper.items import ProductItem

class ProductDetails(scrapy.Spider):
	name = 'amazon_product_scraper'
	start_urls = ['https://www.amazon.fr/s/ref=nb_sb_noss_2?'\
					'url=search-alias%3Daps&field-keywords=macbook']

	def parse(self, reponse):
		search_results = reponse.css('ul.s-result-list > li')
		for product in search_results:
			title = product.css('.s-access-title::text').extract_first()
			link = product.css('a.s-access-detail-page::attr(href)').extract_first()
			price = product.css('.s-price::text').extract_first()

			truncated_title = title[:50]
			product_id = link.split('/')[-1]
			short_link = 'https://amazon.fr/dp/' + product_id

			productItem = ProductItem()
			productItem['title'] = truncated_title
			productItem['link'] = short_link
			productItem['price'] = price

			yield productItem