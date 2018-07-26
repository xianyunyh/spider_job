import scrapy
from tutorial.items import TutorialItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from pyquery import PyQuery as pq
import  json
import  time
import  random
import re
from scrapy.conf import settings
#zhipin 爬虫
class ZhipinSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["m.lagou.com"]
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
        },
        "DEFAULT_REQUEST_HEADERS":{
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Referer':' https://m.lagou.com/search.html',
            'X-Requested-With':"XMLHttpRequest",
            "cookie":"user_trace_token=20180725211521-aa09c44d3ab54bf2bde9654cc6c4ab35; _ga=GA1.3.881896906.1532524522; _ga=GA1.2.881896906.1532524522; _gid=GA1.2.726017449.1532524522; LGUID=20180725211522-c92c8f9d-900c-11e8-a44e-525400f775ce; index_location_city=%E4%B8%8A%E6%B5%B7; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532362837,1532398323,1532418933,1532572655; JSESSIONID=ABAAABAAAFDABFGC547325A2971F2AA49C9A368C145B679; _gat=1; LGSID=20180726124253-5bcf406b-908e-11e8-9ee6-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fm.lagou.com%2Fjobs%2F4741044.html; PRE_LAND=https%3A%2F%2Fm.lagou.com%2Fsearch.html; X_HTTP_TOKEN=1f8ff879c39e0209e7efb23aad68da74; LG_LOGIN_USER_ID=52613e3ab983a93b76c62f27b7f9f49934626b1999bbab20; _putrc=51AF6FA824D5BE21; login=true; unick=%E7%94%B0%E9%9B%B7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532580490; LGRID=20180726124809-182de556-908f-11e8-a494-525400f775ce"
        }
    }
    def parse(self, response):
        js = json.loads(response.body)
        total = js['content']['data']['page']['totalCount']
        items = js['content']['data']['page']['result']
        pc_header = settings.getdict('LAGOU_PC_HEADERS')
        for item in items:
            url = 'https://m.lagou.com/jobs/'
            url += str(item['positionId'])+".html"
            yield Request(url,callback=self.parse_item,meta=item)
        time.sleep(int(random.uniform(60,80)))
    def parse_item(self,response):
        item = TutorialItem()
        q = response.css
        body = response.body.decode("utf-8")
        match_obj = re.search(r'global.companyAddress = \'(.*)\';', body)
        item['address'] = ""
        if match_obj:
            item['address'] = match_obj.group(1)
        item['salary'] = response.meta['salary']
        item['create_time'] = response.meta['createTime']
        item['body'] = q('.positiondesc .content').xpath("string(.)").extract_first()
        item['company_name']  = response.meta['companyName']
        item['postion_id'] = response.url.split("/")[-1].split('.')[0]
        item['position_name'] = response.meta['positionName']
        time.sleep(int(random.uniform(60,80)))
        yield  item
