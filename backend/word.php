<?php
header("Content-Type: application/json;charset=utf-8");
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Origin: *');

echo file_get_contents("http://yehe.37he.cn/api/word.json");
//db.position.update({'educational':'不限'},{$set:{'educational':'不限'}})
