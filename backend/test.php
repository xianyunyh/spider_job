<?php
/**
 * 测试代码编写（整合）
 */
require './vendor/autoload.php';
header("Content-Type: application/json;charset=utf-8");
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Origin: *');

//实例化mongodb
$client = new MongoDB\Client("mongodb://127.0.0.1");

//获取GET参数
$param = $_GET;

//检索条件
$map = [];
if(isset($params['search']) && isset($params['search']['username']) && strlen(trim($params['search']['username'])) > 0){
    //TODO 字段检索
}
if(isset($params['search']) && isset($params['search']['intervalSubData']) && strlen(trim($params['search']['intervalSubData'])) > 0){
    //TODO 时间段搜索
}

//排序 ( 1 升序  -1 降序)
//排序：1升序，-1降序
//$client->sort(['Age' => 1]);
//忽略前n个匹配的文档
//$client->skip(1);
//只返回前n个匹配的文档（limit()与skip()结合使用可实现数据分页功能）
//$client->limit(1);
//匹配文档的总数
//$client->count();
//指定查询索引


//分页操作



//数据查询



//返回数据处理



