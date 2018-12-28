# -*- coding: utf-8 -*-

from scrapy import Request, Spider

class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    # 用户详情页
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
    # 用户关注列表
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset=2980&limit=20'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    start_user = 'excited-vczh'

    def start_requests(self):

        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), callback=self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20), callback=self.parse_follows)

    def parse_user(self, response):
        print(response.text)

    def parse_follows(self, response):
        print(response.text)
