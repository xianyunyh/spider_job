# 爬虫项目

## 免责声明

<font color="red" size="14">本软件仅用于学术研究，但因在中国大陆频频出现爬虫开发者涉诉与违规相关的[新闻](https://github.com/HiddenStrawberry/Crawler_Illegal_Cases_In_China)。<br></font>

<h3>使用者需遵守其所在地的相关法律法规。因违法违规使用造成的一切后果，使用者自行承担</h3>

这个项目是主要自己研究招聘网站上的职位以及对应的需求准备的一个python项目。
项目基于scrapy框架进行爬虫，使用mongodb存储爬取数据。
前端界面使用`vue`编写,后端接口为 php

在线预览地址: [Demo](http://yehe.37he.cn/job/)

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

```shell
pip install -f requirements.txt
```
- 请安装mongodb、redis

- python 请选用3.6+以上的版本。需要的依赖有 pymongo、scrapy、redis、pyquery(后期可能会移除)

- php请安装 [mogodb拓展](http://pecl.php.net/package/mongodb) 并且依赖 [mongodb/mongodb](https://packagist.org/packages/mongodb/mongodb)

  ```shell
  composer require mongodb/mongodb
  ```



### 运行爬虫

```bash
scrapy crawl boss #抓boss
scrapy crawl 51job #抓51job
scrapy crawl lagou #拉钩
```
## windows下其他问题

 1. 出现`Get it with Microsoft Visual C++ Build Tools: http://landinghub.visualstudio.com/visual-cpp-build-tools`

请到[https://www.lfd.uci.edu/~gohlke/pythonlibs/](https://www.lfd.uci.edu/~gohlke/pythonlibs/) 下载对应的whl文件 然后执行 `pip install xxxx.whl`


