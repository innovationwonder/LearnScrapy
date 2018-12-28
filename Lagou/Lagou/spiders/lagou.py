# -*- coding: utf-8 -*-
import scrapy

from Lagou.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = [
        'https://www.lagou.com/zhaopin/Python/{}/?filterOption=3'.format(i) for i in range(1, 31)
    ]
    def parse(self, response):
        # print(response.text)
        item = LagouItem()
        divs = response.xpath('//*[@id="s_position_list"]/ul/li/div[1]')
        for div in divs:
            title = div.xpath('./div[1]/div[1]/a/h3/text()').extract_first()
            location = div.xpath('./div[1]/div[1]/a/span/em/text()').extract_first()
            salary = div.xpath('./div[1]/div[2]/div/span/text()').extract_first()
            company = div.xpath('./div[2]/div[1]/a/text()').extract_first()
            fintance = div.xpath('./div[2]/div[2]/text()').extract_first()

            item['title'] = title.strip()
            item['location'] = location.strip()
            item['salary'] = salary.strip()
            item['company'] = company.strip()
            item['fintance'] = fintance.strip()

            yield item
