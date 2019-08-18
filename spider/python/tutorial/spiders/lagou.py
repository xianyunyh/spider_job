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
        "https://m.lagou.com/search.json?city=%E4%B8%8A%E6%B5%B7&positionName=PHP&pageSize=10",
    ]
    custom_settings = {
        "ITEM_PIPELINES":{
            'tutorial.pipelines.TutorialPipeline': 300,
        },
        "DOWNLOADER_MIDDLEWARES":{
            #'tutorial.middlewares.LagouMiddleware': 299,
        },
        "DEFAULT_REQUEST_HEADERS":{
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Referer':' https://m.lagou.com/search.html',
            'X-Requested-With':"XMLHttpRequest",
            "cookie":"user_trace_token=20180729204908-c52cbd0e4d394a3cb58519920e083a0b; JSESSIONID=ABAAABAAAGCABCC79240AC570FA1732FC9159DD43105445; X_HTTP_TOKEN=5338df7c911167920d5f0d7615b94748; _ga=GA1.2.1539481412.1532868549; _gid=GA1.2.309176990.1532868549; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532398323,1532418933,1532572655,1532868549; LGSID=20180729204908-c8b50abb-932d-11e8-ab47-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fts%3D1532868548009%26serviceId%3Dlagou%26service%3Dhttp%25253A%25252F%25252Fm.lagou.com%25252Fuser%25252Fcollect.json%25253FpositionId%25253D233753%26action%3Dlogin%26signature%3D01759552449CC48F903E9AB889298EAC; LGUID=20180729204908-c8b50c64-932d-11e8-ab47-525400f775ce; _ga=GA1.3.1539481412.1532868549; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532868713; LGRID=20180729205153-2ae970a6-932e-11e8-a07d-5254005c3644"
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
            print(url)
            time.sleep(int(random.uniform(160,180)))
            yield Request(url,callback=self.parse_item,meta=item,headers=pc_header)
        if self.current_page < 4:
            self.current_page += 1
            list_url = self.start_urls[0]+"&pageNo="+str(self.current_page)
            time.sleep(int(random.uniform(160,180)))
            yield Request(list_url,callback=self.parse)
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
        item['body'] = q('.content').xpath('string(.)').extract_first()
        item['company_name']  = response.meta['companyName']
        item['postion_id'] = response.meta['positionId']
        item['position_name'] = response.meta['positionName']
    #print(item)
        yield  item
