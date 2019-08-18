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
        "https://www.zhipin.com/mobile/jobs.json?city=101020100&query=PHP",
    ]
    custom_settings = {
        "ITEM_PIPELINES":{
            'tutorial.pipelines.ZhipinPipeline': 300,
        },
        "DOWNLOADER_MIDDLEWARES":{
            'tutorial.middlewares.ZhipinMiddleware': 299,
            #'tutorial.middlewares.ProxyMiddleware':301
        },
        "DEFAULT_REQUEST_HEADERS":{
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent':'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Mobile Safari/537.36',
            'Referer':'https://www.zhipin.com/',
            'X-Requested-With':"XMLHttpRequest",
            "cookie":"lastCity=101020100; JSESSIONID=""; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1532401467,1532435274,1532511047,1532534098; __c=1532534098; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fc101020100-p100103%2F; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1532581213; __a=4090516.1532500938.1532516360.1532534098.11.3.7.11"
        }
    }

    def parse(self, response):
        js = json.loads(response.body)
        html = js['html']
        q = pq(html)
        items = q(".item")
        host = 'https://www.zhipin.com'
        x = 1
        item = items[0]
        url = host + q(item).find('a').attr('href')
        position_name = q(item).find('.title h4').text()
        salary = q(item).find('.salary').text() or  ''
        work_year = q(item).find('.msg em').eq(1).text() or '不限'
        educational = q(item).find('.msg em').eq(2).text()

        meta = {
            "position_name":position_name,
            "salary":salary,
            "work_year":work_year,
            "educational":educational
        }
        #time.sleep(int(random.uniform(50, 70)))
        yield Request(url,callback=self.parse_item,meta=meta)
        pass
    def parse_item(self,response):
            item = TutorialItem()
            q = response.css
            item['address'] = q('.location-address::text').extract_first()
            item['create_time'] = q('.job-tags .time::text').extract_first()
            item['body'] = q('.text').xpath('string(.)').extract_first()
            item['company_name']  = q('.business-info h4::text').extract_first()
            item['postion_id'] = response.url.split("/")[-1].split('.')[0]
            item = dict(item, **response.meta )
            yield  item
