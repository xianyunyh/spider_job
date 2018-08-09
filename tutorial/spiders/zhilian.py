import scrapy
from tutorial.items import TutorialItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy.conf import settings
import  json
import  time
import  random


#zhilian 爬虫
class TestSpider(scrapy.Spider):
    name = "zhilian"
    allowed_domains = ["m.zhaopin.com"]
    current_page = 1
    # 上海PHP
    start_urls = [
        "https://m.zhaopin.com/shanghai-538/?keyword=php&pageindex=1&maprange=3&islocation=0&order=0",
    ]
    custom_settings = {
        "ITEM_PIPELINES":{
            'tutorial.pipelines.TutorialPipeline': 300,
        },
        "DOWNLOADER_MIDDLEWARES":{
            #'tutorial.middlewares.ZhipinMiddleware': 299,
            #'tutorial.middlewares.ProxyMiddleware':301
        },
        "DEFAULT_REQUEST_HEADERS":{
            #'Accept': 'application/json',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent':'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Mobile Safari/537.36',
            'Referer':'https://www.zhipin.com/',
            'X-Requested-With':"XMLHttpRequest",
            'cookie':'dywez=95841923.1533431793.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined; _ga=GA1.2.1761807953.1533431793; __utmz=269921210.1533431793.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); platform=7; dywea=95841923.2388848959108036000.1533431793.1533434029.1533822603.3; dywec=95841923; adfbid=0; adfbid2=0; _gid=GA1.2.764667090.1533822603; __utma=269921210.1761807953.1533431793.1533434029.1533822603.3; __utmc=269921210; __utmt=1; sts_deviceid=1651f05772f519-0941841dbb2174-2711938-1327104-1651f05773034; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; sts_sg=1; sts_sid=1651f0577e0304-001af92ed86852-2711938-1327104-1651f0577e1250; __utmb=269921210.40.9.1533822928919; dyweb=95841923.40.8.1533822927269; ZP_OLD_FLAG=false; zp_src_url=https%3A%2F%2Fwww.zhaopin.com%2F; GUID=fbb54f2b54a5459da14aa9b177b9c83a; LastCity=%E4%B8%8A%E6%B5%B7; LastCity%5Fid=538; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1533823781; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1533823781; sts_evtseq=10; ZL_REPORT_GLOBAL={%22sou%22:{%22actionIdFromSou%22:%22aae3d7a4-6197-4c76-9306-5a9fad4c5e6a-sou%22%2C%22funczone%22:%22latest_jd%2'
        }
    }

    def parse(self, response):
        items = response.css("#r_content section")

        for item in items:
            host = "https://m.zhaopin.com"
            url  =  host + item.xpath('//a/@data-link').extract_first()
            print(url)
            yield Request(url,callback=self.parse_item)
        pass
    def parse_item(self,response):
            item = TutorialItem()
            q = response.css
            item['address'] = q('.add::text').extract_first()
            item['create_time'] = q('.job-detail .time::text').extract_first()
            item['body'] = q('.text').xpath('string(.)').extract_first()
            item['company_name']  = q('.add::text').extract_first()
            item['salary'] = q('.job-sal::text').extract_first()
            item['work_year'] = q('.job-detail .exp::text').extract_first()
            item['educational'] = q('.job-detail span:nth-child(3)::text').extract_first()
            item['postion_id'] = response.url.split("/")[-1]
            item['body'] = q('.about-main::text').extract_first()
            #item = dict(item, **response.meta )
            yield  item
