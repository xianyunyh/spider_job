# 爬虫项目
这个项目是主要自己研究招聘网站上的职位以及对应的需求准备的一个python项目。

数据来源为拉钩和直聘网。
项目基于scrapy框架进行爬虫，使用mongodb存储爬取数据。

- 项目目录结构图

```

├─backend php后端接口
├─front 前端界面
│  ├─job                vue
│  ├─company.html       热门公司
│  ├─education.html     学历分析
│  ├─weekline.html      发布趋势
├─tutorial python爬虫
│  ├─spiders           爬虫
│  │  ├─51job.py       51job爬虫
│  │  ├─lagou.py       拉钩爬虫
│  │  ├─zhipin.py      直聘爬虫
│  ├─items.py          数据项
│  ├─middlewares.py    中间件
│  ├─pipelines.py      管道
│  ├─settings.py       项目配置
├─word.json 生成的英文技术词json
├─word.py 生成英文分词
├─stop.txt 停用词列表
```

## 安装

- 请安装mongodb、redis

- python 请选用3.6+以上的版本。需要的依赖有 pymongo、scrapy、redis、pyquery(后期可能会移除)

- php请安装pecl [mogodb拓展](http://pecl.php.net/package/mongodb)！依赖 [mongodb/mongodb](https://packagist.org/packages/mongodb/mongodb)

  ```
  composer require mongodb/mongodb
  ```



运行爬虫

```bash
scrapy crawl boss #抓boss
scrapy crawl 51job #抓51job
scrapy crawl lagou #拉钩
```

