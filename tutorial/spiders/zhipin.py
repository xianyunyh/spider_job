import scrapy
from tutorial.items import TutorialItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
import  json
import  time
import  random
import redis
from scrapy.conf import settings

#zhipin 爬虫
class ZhipinSpider(scrapy.Spider):

    name = "boss"
    allowed_domains = ["www.zhipin.com"]

    current_page = 1 #开始页码
    max_page = 4 #最大页码
    start_urls = [
        "https://www.zhipin.com/mobile/jobs.json?city=101020100&query=PHP",
    ]
    custom_settings = {
        "ITEM_PIPELINES":{
            'tutorial.pipelines.ZhipinPipeline': 300,
        },
        "DOWNLOADER_MIDDLEWARES":{
            'tutorial.middlewares.ZhipinMiddleware': 299,
         #   'tutorial.middlewares.ProxyMiddleware':301
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

        q = Selector(text=html)


        items = q.css(".item")

        host = 'https://www.zhipin.com'
        x = 1
        for item in items:
            url = host + item.xpath('//a/@href').extract_first()

            position_name = item.css('h4::text').extract_first() #职位名称
            salary = item.css('.salary::text').extract_first() or  '' #薪资
            work_year = item.css('.msg em:nth-child(2)::text').extract_first() or '不限' #工作年限
            educational = item.css('.msg em:nth-child(3)::text').extract_first() #教育程度
            meta = {
                "position_name":position_name,
                "salary":salary,
                "work_year":work_year,
                "educational":educational
            }

            time.sleep(int(random.uniform(50, 70)))
            #初始化redis
            pool= redis.ConnectionPool(host='localhost',port=6379,decode_responses=True)
            r=redis.Redis(connection_pool=pool)
            key = settings.get('REDIS_POSITION_KEY')
            position_id = url.split("/")[-1].split('.')[0]
            if (r.sadd(key,position_id)) == 1:
                yield Request(url,callback=self.parse_item,meta=meta)

        if self.current_page < self.max_page:
            self.current_page += 1
            api_url = "https://www.zhipin.com/mobile/jobs.json?city=101020100&query=PHP"+"&page="+str(self.current_page)
            time.sleep(int(random.uniform(50, 70)))
            yield  Request(api_url,callback=self.parse)
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
