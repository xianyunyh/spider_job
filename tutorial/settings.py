# -*- coding: utf-8 -*-

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
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
    'X-Requested-With':"XMLHttpRequest"
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
HTTP_PROXY = 'http://47.104.84.76:8888/'

LAGOU_HEADERS = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'user-agent:':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer':' https://m.lagou.com/search.html',
    'X-Requested-With':"XMLHttpRequest",
    "cookie":"user_trace_token=20180725211521-aa09c44d3ab54bf2bde9654cc6c4ab35; JSESSIONID=ABAAABAAAFDABFG1E48EFB2B4DAB3779F335D20F2F3CBFC; _ga=GA1.3.881896906.1532524522; _gat=1; _ga=GA1.2.881896906.1532524522; _gid=GA1.2.726017449.1532524522; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532356116,1532362837,1532398323,1532418933; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532524522; LGSID=20180725211522-c92c8db7-900c-11e8-a44e-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fm.lagou.com%2F; PRE_LAND=https%3A%2F%2Fm.lagou.com%2Fsearch.html; LGUID=20180725211522-c92c8f9d-900c-11e8-a44e-525400f775ce; LGRID=20180725211537-d21577e4-900c-11e8-a44e-525400f775ce"
}
LAGOU_COOKIE = "user_trace_token=20180725211521-aa09c44d3ab54bf2bde9654cc6c4ab35; JSESSIONID=ABAAABAAAFDABFG1E48EFB2B4DAB3779F335D20F2F3CBFC; _ga=GA1.3.881896906.1532524522; _gat=1; _ga=GA1.2.881896906.1532524522; _gid=GA1.2.726017449.1532524522; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532356116,1532362837,1532398323,1532418933; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532524522; LGSID=20180725211522-c92c8db7-900c-11e8-a44e-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fm.lagou.com%2F; PRE_LAND=https%3A%2F%2Fm.lagou.com%2Fsearch.html; LGUID=20180725211522-c92c8f9d-900c-11e8-a44e-525400f775ce; LGRID=20180725211537-d21577e4-900c-11e8-a44e-525400f775ce"

LAGOU_PC_HEADERS = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/53",
    "Upgrade-Insecure-Requests":1,
    "Cookie":"showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=48; JSESSIONID=ABAAABAAAIAACBI765D21AAD55C912AFCF7A5B6C9E3528E; user_trace_token=20180725211521-aa09c44d3ab54bf2bde9654cc6c4ab35; _ga=GA1.2.881896906.1532524522; _gid=GA1.2.726017449.1532524522; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532356116,1532362837,1532398323,1532418933; LGUID=20180725211522-c92c8f9d-900c-11e8-a44e-525400f775ce; X_HTTP_TOKEN=1f8ff879c39e0209e7efb23aad68da74; index_location_city=%E4%B8%8A%E6%B5%B7; TG-TRACK-CODE=search_code; LGSID=20180725224409-305b77fe-9019-11e8-a453-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fts%3D1532529848384%26serviceId%3Dlagou%26service%3Dhttp%25253A%25252F%25252Fwww.lagou.com%25252Fsearch.html%26action%3Dlogin%26signature%3DECAD154F112F1197B45E75CB80D8B5BF; _gat=1; SEARCH_ID=626c0a2024964c54b75f4a8aadaaa15d; LGRID=20180725224533-6231ff52-9019-11e8-a453-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1532529933",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer":"https://www.lagou.com/zhaopin/PHP/"
}
