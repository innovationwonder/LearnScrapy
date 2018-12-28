# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quote' # 每个项目唯一的名字，用来区分不同的 Spider
    allowed_domains = ['quotes.toscrape.com'] # 允许爬取的域名，可以过滤掉不是这个域名下的请求
    start_urls = ['http://quotes.toscrape.com/'] # 启动时爬取的 url 列表

    def parse(self, response):
        '''
        默认下，被调用时，
        start_urls 里的链接构成请求 完成下载后，返回的 response 就会作为唯一的参数传递给这个函数
        该方法负责解析返回的 response、提取数据/进一步生成要处理的请求
        :param response:
        :return:
        '''
        quotes = response.css('.quote') # 选取所有 quote 区块
        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()

            yield item

        next = response.css('.pager .next a::attr(href)').extract_first() # 从 response 中提取 下一页的链接
        url = response.urljoin(next) # urljoin() 可以将相对 url 构造成绝对 URL
        yield scrapy.Request(url=url, callback=self.parse) # 构造了一个新的请求,请求完成后，响应会重新经过 parse() 方法处理，再生成下一页，循环到最后一页

