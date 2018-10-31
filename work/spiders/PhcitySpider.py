# -*- coding: utf-8 -*-
import scrapy
from work.work.items import PhCityItem

class PhcityspiderSpider(scrapy.Spider):
    name = 'PhcitySpider'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/List_of_Philippine_city_name_etymologies']

    def parse(self, response):
        sel = scrapy.Selector(response)
        for url in response.xpath("//table//tr/td/b/a/@href").extract():
            yield scrapy.Request(url,callback=self.getParam)

    def getParam(self,response):
        sel = scrapy.Selector(response)
        param = response.xpath('//table/tbody/tr/th/span[@class="fn org"]').extract()
        return PhCityItem(cityName=param)