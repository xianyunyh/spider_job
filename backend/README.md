## php后端API接口

- /api/company.php 获取最新热门公司接口
- /api/education.php 获取招聘学历情况
- /api/monthline.php 获取月度统计
- /api/weekdayline.php 获取一周数据
- /api/word.php 热门关键词

## 安装

需要安装`mongodb` 拓展 和 `mongodb/mongodb` composer 依赖包

- [https://pecl.php.net/package/mongodb](https://pecl.php.net/package/mongodb)
- [mongodb/mongodb](https://packagist.org/packages/mongodb/mongodb) composer依赖

```shell
composer require mongodb/mongodb
composer dumpautload
```
## 使用
```php
$config = [
    "uri"=>"mongodb://127.0.0.1",
    "db"=>"job",
    "collection"=>"postion",
]
$store = new Boss\Store($config);

```