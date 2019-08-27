<?php
require_once "./vendor/autoload.php";
use Boss\Job;
use MongoDB\Client;
$config = [
    "uri"=>"mongodb://root:123456@mongodb",
    "db"=>"job",
    "collection"=>"position",
];
header("Content-Type: application/json;charset=utf-8");
$arr = file("./datas.json");
$client = new MongoDB\Client($config['uri']);
$company = $client->job->company;

$data = [];

$res = $company->find();
foreach ($res as $doc) {
    $data[] = [
        "lnglat"=>[floatval($doc['position_lng']),floatval($doc['position_lat'])],
        "name"=>$doc["company_name"],
    ];
}

echo json_encode($data);