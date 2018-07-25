import scrapy
from tutorial.items import TutorialItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from pyquery import PyQuery as pq
import  json
import  time
import  random

#zhipin 爬虫
class ZhipinSpider(scrapy.Spider):
    name = "boss"
    allowed_domains = ["www.zhipin.com"]

    current_page = 1
    start_urls = [
        "https://www.zhipin.com/mobile/jobs.json?city=101020100&query=PHP",
    ]

    def parse(self, response):
        js = json.loads(response.body)
        html = js['html']
        q = pq(html)
        items = q(".item")
        host = 'https://www.zhipin.com'
        x = 1
        for item in items:
            url = host + q(item).find('a').attr('href')
            time.sleep(int(random.uniform(5, 10)))
            yield Request(url,callback=self.parse_item)

        if self.current_page < 20:
            self.current_page += 1
            api_url = self.start_urls[0]+"&page="+str(self.current_page)
            time.sleep(int(random.uniform(5, 10)))
            yield  Request(api_url,callback=self.parse)
        pass

    def parse_item(self,response):
        item = TutorialItem()
        q = response.css
        item['address'] = q('.location-address::text').extract_first()
        item['salary'] = q('.salary::text').extract_first()
        item['create_time'] = q('.job-tags .time::text').extract_first()
        item['body'] = q('.text::text').extract_first()
        item['company_name']  = q('.business-info h4::text').extract_first()
        item['postion_id'] = response.url.split("/")[-1].split('.')[0]
        yield  item
