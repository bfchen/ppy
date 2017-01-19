# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


from my_crawler.items import MyCrawlerItem

class MyCrawlSpider(CrawlSpider):
    """docstring for MyCrawlSpider"""

    name = "my_crawler"
    allowed_domains = ['bjhee.com']
    start_urls = ["http://www.bjhee.com",]

    rules = (
        Rule(LinkExtractor(allow=r'/page/[0-9]+'),
            callback = 'parse_item',
            follow = True
        ),
    )

    def parse_item(self, response):
        articles = response.xpath('//*[@id="main"]/ul/li')

        for article in articles:
            item = MyCrawlerItem()
            item['title'] = article.xpath('h3[@class="entry-title"]/a/text()').exttact()[0]
            item['url'] = article.xpath('h3[@class="entry-title"]/a/href').exttact()[0]
            item['summary']=article.article.xpath('div[2]/p/text()').exttact()[0]
            yield item

