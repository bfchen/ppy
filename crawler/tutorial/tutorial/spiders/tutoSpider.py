# -*- coding: UTF-8 -*-
import scrapy,sys
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import TutorialItem

#设置编码格式
reload(sys)
sys.setdefaultencoding('gbk')

class TutoSpider(Spider):
    name = "tutoSpider"
    allowed_domains = ["dmoz.org"]
    start_urls = [
                  "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
                  "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
                  ]
def parse(self, response):
  
    """
    The lines below is a spider contract. For more info see:
    http://doc.scrapy.org/en/latest/topics/contracts.html
    @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
    @scrapes name
    """
    sel = Selector(response)
    sites = sel.xpath('//ul/li')
    for site in sites:
        title = site.xpath('a/text()').extract()
        link = site.xpath('a/@href').extract()
        disc = site.xpath('text()').extract()
        print("title= "+str(title)+"\tlink= "+str(link)+"\tdisc= "+str(disc)+"\n")
