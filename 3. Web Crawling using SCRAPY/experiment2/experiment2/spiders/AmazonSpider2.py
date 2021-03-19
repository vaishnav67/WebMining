import scrapy
class AmazonItems(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    discount_price = scrapy.Field()
    image = scrapy.Field()
class Amazonspider2Spider(scrapy.Spider):
    name = 'AmazonSpider'
    allowed_domains = ['https://www.amazon.in/dp/B082X8LLP7/']
    start_urls = ['https://www.amazon.in/dp/B082X8LLP7/']
    def parse(self, response):
        items = AmazonItems()
        items['name'] = response.css('.product-title-word-break::text').extract_first()
        items['name'] = items['name'].replace(u'\n', u'')
        items['price'] = response.css('.priceBlockStrikePriceString::text').extract_first()
        items['price'] = items['price'].replace(u'\xa0', u'')
        items['discount_price'] = response.css('.priceBlockBuyingPriceString::text').extract_first()
        items['discount_price'] = items['discount_price'].replace(u'\xa0', u'')
        items['image'] = response.css('.a-dynamic-image::attr(src)').extract_first()
        yield items
