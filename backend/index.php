<?php
require_once "./vendor/autoload.php";
use Boss\Job;
$config = [
    "uri"=>"mongodb://root:123456@mongodb",
    "db"=>"job",
    "collection"=>"position",
];
header("Content-Type: application/json;charset=utf-8");
try {
    $store = new Job($config);
    $data = $store->getWeekLine(new DateTimeImmutable("2019-08-18"),new DateTimeImmutable("2019-08-18"));
    echo json_encode($data);
}catch ( Exception $e) {
    echo $e->getMessage();
}
