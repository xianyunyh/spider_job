import scrapy
from tutorial.items import TutorialItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
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
    start_urls = [
        "https://www.zhipin.com/mobile/jobs.json?city="+settings.get("BOSS_CITY_CODE")+"&query="+settings.get("LANGUAGE"),
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
            'User-Agent':'Mozilla/5.0 (Linux; Android 9.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Mobile Safari/537.36',
            'Referer':'https://www.zhipin.com/',
            'X-Requested-With':"XMLHttpRequest",
            "cookie":"lastCity=101020100; JSESSIONID=""; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1532401467,1532435274,1532511047,1532534098; __c=1532534098; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=; toUrl=https%3A%2F%2Fwww.zhipin.com%2Fc101020100-p100103%2F; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1532581213; __a=4090516.1532500938.1532516360.1532534098.11.3.7.11"
        }
    }
    def parse(self, response):
        js = json.loads(response.body)
        html = js['html']
        q = Selector(text=html)
        items = q.css('.item')
        host = 'https://www.zhipin.com'
        x = 1
        redis_host = settings.get('REDIS_HOST')
        redis_port = settings.get('REDIS_PORT')
        #初始化redis
        pool= redis.ConnectionPool(host=redis_host,port=redis_port,decode_responses=True)
        r=redis.Redis(connection_pool=pool)
        setkey = settings.get('REDIS_POSITION_KEY')
        for item in items:
            url = host + item.css('a::attr(href)').extract_first()
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
            sleep_seconds = int(settings.get('SLEEP_SECONDS'))
            time.sleep(int(random.uniform(sleep_seconds, sleep_seconds+20)))

            position_id = url.split("/")[-1].split('.')[0]
            print(position_id)
            if (r.sadd(setkey,position_id)) == 1:
                yield Request(url,callback=self.parse_item,meta=meta)
        max_page = settings.get('MAX_PAGE')
        if self.current_page < max_page:
            self.current_page += 1
            api_url = "https://www.zhipin.com/mobile/jobs.json?city="+settings.get("BOSS_CITY_CODE")+"&query="+settings.get("LANGUAGE")+"&page="+str(self.current_page)
            time.sleep(int(random.uniform(sleep_seconds, sleep_seconds+20)))
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
