import scrapy
from tutorial.items import TutorialItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from pyquery import PyQuery as pq
import  json
import  time
import  random
from scrapy.conf import settings
#zhipin 爬虫
class ZhipinSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["www.lagou.com"]
    current_page = 1
    # 上海PHP
    start_urls = [
        "https://m.lagou.com/search.json?city=%E4%B8%8A%E6%B5%B7&positionName=PHP&pageSize=50&pageNo=1",
    ]
    custom_settings = {
        "ITEM_PIPELINES":{
            'tutorial.pipelines.TutorialPipeline': 300,
        },
        "DOWNLOADER_MIDDLEWARES":{
            'tutorial.middlewares.LagouMiddleware': 299,
        }
    }
    def parse(self, response):
        js = json.loads(response.body)
        total = js['content']['data']['page']['totalCount']
        items = js['content']['data']['page']['result']

        pc_header = settings.getdict('LAGOU_PC_HEADERS')
        for item in items:
            url = 'https://www.lagou.com/jobs/'
            url += str(item['positionId'])+".html"
            yield Request(url,callback=self.parse_item,meta=item,headers=pc_header)
            time.sleep(1)

    def parse_item(self,response):
        item = TutorialItem()
        q = response.css
        item['address'] = "".join(q('.work_addr::text').extract())
        item['salary'] = "".join(q('.job_request .salary::text').extract())
        item['create_time'] = "".join(q('.publish_time::text').extract())
        item['body'] = "".join(q('.job_bt::text').extract())
        item['company_name']  = "".join(q('.publisher_name .name::text').extract())
        item['postion_id'] = response.url.split("/")[-1].split('.')[0]
        yield  item
