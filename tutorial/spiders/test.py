import scrapy
from tutorial.items import TutorialItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from pyquery import PyQuery as pq
import  json
import  time
import  random
from scrapy.conf import settings
import re
#zhipin 爬虫
class TestSpider(scrapy.Spider):
    name = "test"
    # allowed_domains = ["www.lagou.com"]
    current_page = 1
    # 上海PHP
    start_urls = [
        "https://m.lagou.com/jobs/4710408.html",
    ]
    custom_settings = {
        "ITEM_PIPELINES":{
           # 'tutorial.pipelines.TutorialPipeline': 300,
        },
        "DOWNLOADER_MIDDLEWARES":{
            'tutorial.middlewares.LagouMiddleware': 299,
        }
    }

    def parse(self, response):
        body = response.body.decode("utf-8")
        print((body))
        match_obj = re.search(r'global.companyAddress = \'(.*)\';', body)
        if match_obj:
            Forge_Token = match_obj.group(1)
        print(Forge_Token)
        pass
