# -*- coding: utf-8 -*-

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

LOG_LEVEL = 'ERROR'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'user-agent:':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':' https://m.lagou.com/search.html',
    'X-Requested-With':"XMLHttpRequest",
    "cookie":"user_trace_token=20180725211521-aa09c44d3ab54bf2bde9654cc6c4ab35; _ga=GA1.3.881896906.1532524522; _ga=GA1.2.881896906.1532524522; _gid=GA1.2.726017449.1532524522; LGUID=20180725211522-c92c8f9d-900c-11e8-a44e-525400f775ce; index_location_city=%E4%B8%8A%E6%B5%B7; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532362837,1532398323,1532418933,1532572655; JSESSIONID=ABAAABAAAFDABFGC547325A2971F2AA49C9A368C145B679; _gat=1; LGSID=20180726124253-5bcf406b-908e-11e8-9ee6-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fm.lagou.com%2Fjobs%2F4741044.html; PRE_LAND=https%3A%2F%2Fm.lagou.com%2Fsearch.html; X_HTTP_TOKEN=1f8ff879c39e0209e7efb23aad68da74; LG_LOGIN_USER_ID=52613e3ab983a93b76c62f27b7f9f49934626b1999bbab20; _putrc=51AF6FA824D5BE21; login=true; unick=%E7%94%B0%E9%9B%B7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532580490; LGRID=20180726124809-182de556-908f-11e8-a494-525400f775ce"
}
USER_AGENT_LIST = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
]
FEED_EXPORT_ENCODING = 'utf-8'

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   #'tutorial.middlewares.ProxyMiddleware': 543,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
  # 'tutorial.middlewares.ProxyMiddleware': 299,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#   'tutorial.pipelines.TutorialPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTP_PROXY = 'http://127.0.0.1:8123/'

LAGOU_HEADERS = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'user-agent:':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':' https://m.lagou.com/search.html',
    'X-Requested-With':"XMLHttpRequest",
    "cookie":"user_trace_token=20180725211521-aa09c44d3ab54bf2bde9654cc6c4ab35; JSESSIONID=ABAAABAAAFDABFG1E48EFB2B4DAB3779F335D20F2F3CBFC; _ga=GA1.3.881896906.1532524522; _gat=1; _ga=GA1.2.881896906.1532524522; _gid=GA1.2.726017449.1532524522; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532356116,1532362837,1532398323,1532418933; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532524522; LGSID=20180725211522-c92c8db7-900c-11e8-a44e-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fm.lagou.com%2F; PRE_LAND=https%3A%2F%2Fm.lagou.com%2Fsearch.html; LGUID=20180725211522-c92c8f9d-900c-11e8-a44e-525400f775ce; LGRID=20180725211537-d21577e4-900c-11e8-a44e-525400f775ce"
}
LAGOU_COOKIE = "user_trace_token=20180725211521-aa09c44d3ab54bf2bde9654cc6c4ab35; _ga=GA1.3.881896906.1532524522; _ga=GA1.2.881896906.1532524522; _gid=GA1.2.726017449.1532524522; LGUID=20180725211522-c92c8f9d-900c-11e8-a44e-525400f775ce; index_location_city=%E4%B8%8A%E6%B5%B7; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532362837,1532398323,1532418933,1532572655; JSESSIONID=ABAAABAAAFDABFGC547325A2971F2AA49C9A368C145B679; _gat=1; LGSID=20180726124253-5bcf406b-908e-11e8-9ee6-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fm.lagou.com%2Fjobs%2F4741044.html; PRE_LAND=https%3A%2F%2Fm.lagou.com%2Fsearch.html; X_HTTP_TOKEN=1f8ff879c39e0209e7efb23aad68da74; LG_LOGIN_USER_ID=52613e3ab983a93b76c62f27b7f9f49934626b1999bbab20; _putrc=51AF6FA824D5BE21; login=true; unick=%E7%94%B0%E9%9B%B7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532580189; LGRID=20180726124308-650bb11a-908e-11e8-9ee6-5254005c3644"

LAGOU_PC_HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/53",
    "Upgrade-Insecure-Requests":1,
    "Cookie":"user_trace_token=20180725211521-aa09c44d3ab54bf2bde9654cc6c4ab35; _ga=GA1.3.881896906.1532524522; _ga=GA1.2.881896906.1532524522; _gid=GA1.2.726017449.1532524522; LGUID=20180725211522-c92c8f9d-900c-11e8-a44e-525400f775ce; index_location_city=%E4%B8%8A%E6%B5%B7; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532362837,1532398323,1532418933,1532572655; JSESSIONID=ABAAABAAAFDABFGC547325A2971F2AA49C9A368C145B679; _gat=1; LGSID=20180726124253-5bcf406b-908e-11e8-9ee6-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fm.lagou.com%2Fjobs%2F4741044.html; PRE_LAND=https%3A%2F%2Fm.lagou.com%2Fsearch.html; X_HTTP_TOKEN=1f8ff879c39e0209e7efb23aad68da74; LG_LOGIN_USER_ID=52613e3ab983a93b76c62f27b7f9f49934626b1999bbab20; _putrc=51AF6FA824D5BE21; login=true; unick=%E7%94%B0%E9%9B%B7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532580490; LGRID=20180726124809-182de556-908f-11e8-a494-525400f775ce",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer":"https://www.lagou.com/zhaopin/PHP/"
}

BOSS_COOKIE = "lastCity=101020100; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1532661872,1532686206; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1532687462; __g=-; __l=%22r=https%3A%2F%2Fwww.zhipin.com%2F&l=%2Fc101020100-p100103%2F%22; __a=15569087.1532687461..1532687461.1.1.1.1"

REDIS_POSITION_KEY = "positionIds"

# 最大的页数
MAX_PAGE = 4;
#sleep的时间间隔
SLEEP_SECONDS=50;
# 抓取的语言
LANGUAGE = "PHP"
#上海
BOSS_CITY_CODE = "101020100"

# REDIS
REDIS_HOST="127.0.0.1"
REDIS_PORT="6379"
#mongodb