import scrapy
from tutorial.items import TutorialItem
from scrapy.http import Request

#zhipin 爬虫
class FiveJobSpider(scrapy.Spider):
    name = "51job"
    allowed_domains = ["m.51job.com"]
    current_page = 1
    max_page = 20
    # 上海PHP
    start_urls = [
        "https://m.51job.com/search/joblist.php?jobarea=020000&keyword=PHP&pageno=1",
    ]
    custom_settings = {
        "ITEM_PIPELINES":{
            'tutorial.pipelines.FiveJobPipeline': 300,
        },
        "DOWNLOADER_MIDDLEWARES":{
            #'tutorial.middlewares.LagouMiddleware': 299,
        },
        "DEFAULT_REQUEST_HEADERS":{
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Referer':'https://m.51job.com/',
            #'X-Requested-With':"XMLHttpRequest",
            "cookie":"guid=15313625525334480016; _ujz=OTE2MjUyNjgw; ps=us%3DWmdaOVUpVGABYQFrUSpTYQU2BilQZABlAjxTfQw3DjtcZwBqAmNRYVQ3WjNQMAY3V2EAMlVmAitSHlN1CkwAdloC%26%7C%26needv%3D0; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; apxlp=1; partner=tg_yunos_mz; slife=lastlogindate_m%3D20180804%26%7C%26; indexfloatpage=indexlogin%3D20180804%26%7C%26indexwx%3D20180804; 51job=cenglish%3D0%26%7C%26; search=jobarea%7E%60020000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA020000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAPHP+%BF%AA%B7%A2%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1532243629%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA020000%2C00%A1%FB%A1%FA020300%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA08%2C09%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAPHP%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1532333324%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch2%7E%601%A1%FB%A1%FA020000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA08%2C09%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAPHP%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1531708646%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch3%7E%601%A1%FB%A1%FA020000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA09%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAPHP%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1531708638%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch4%7E%601%A1%FB%A1%FA020000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA08%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FAPHP%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1531708594%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21collapse_expansion%7E%601%7C%21; m_search=keyword%3DPHP+%E5%BC%80%E5%8F%91%26%7C%26areacode%3D020000"
        }
    }
    def parse(self, response):
        q = response.css
        items = q(".items a").xpath("@href").extract()
        for url in items:
            yield  Request(url,callback=self.parse_item)

        if self.current_page < self.max_page:
            self.current_page += 1
            nex_page = 'https://m.51job.com/search/joblist.php?jobarea=020000&keyword=PHP&pageno='+str(self.current_page)
            yield Request(nex_page,callback=self.parse)
    def parse_item(self,response):
        item =  TutorialItem()
        q = response.css
        item['address'] = q('.jt em::text').extract_first() + ' ' +q('.rec span::text').extract_first()
        item['salary'] = q('.jp::text').extract_first()
        item['create_time'] = q('.jt span::text').extract_first()
        item['body']  = q('.ain article').xpath('string(.)').extract_first()
        item['company_name'] = q('.rec .c_444::text').extract_first()
        item['postion_id'] = response.url.split("/")[-1].split('.')[0]
        item['position_name'] = q('.jt p::text').extract_first()
        item['work_year'] = q('.jd .s_n::text').extract_first() or "不限"
        item['educational']  = q('.jd .s_x::text').extract_first() or "不限"
        print(item['postion_id'])
        yield  item
