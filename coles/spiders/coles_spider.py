from urllib.parse import urljoin
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from coles.items import ColesItem
from coles.settings import REQUIRED_IMAGES



class ColesSpider(CrawlSpider):
    name = "coles"
    start_urls = (
        'https://www.coles.com.au/',
    )
    rules = (
        Rule(LinkExtractor(allow=()), callback="parse_items", follow=False),
    )

    def __init__(self, urls='', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = urls.split(',')

    def parse_items(self, response):
        content = scrapy.Selector(response=response).xpath('//body')
        for nodes in content:
            # build absolute URLs
            img_urls = [urljoin(response.url, src)
                        for src in nodes.xpath('//img/@src').extract()]

            item = ColesItem()
            required_image_url = []
            for img_url in img_urls:
                if img_url in REQUIRED_IMAGES:
                    required_image_url.append(img_url)
            item['image_urls'] = required_image_url
            yield item
