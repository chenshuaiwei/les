# -*- coding: utf-8 -*-
import scrapy


class BlogSpider(scrapy.Spider):
    name = "blog"
    allowed_domains = ["lesmecsdecokto.blogspot.com"]
    start_urls = (
        'http://www.lesmecsdecokto.blogspot.com/',
    )

    def parse(self, response):
        pass
