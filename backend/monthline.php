<?php
require './vendor/autoload.php';
header("Content-Type: application/json;charset=utf-8");
header('Access-Control-Allow-Origin: *');
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
header('Access-Control-Allow-Methods: GET, POST, PUT,DELETE');
$client = new MongoDB\Client("mongodb://127.0.0.1");

$collection = $client->job->position;

$today = date("Y-m-d");
$beforeWeek = date("Y-m-d", strtotime(" 6 months ago"));
$where = [
    "create_time" => [
        '$gt' => "2018-07-24",
    ],
];

$cursor = $collection->aggregate(
    [
        ['$match' => ['create_time' => ['$gte' => $beforeWeek, '$lte' => $today]]],
        ['$group' => ['_id' => [
          '$substr'=>['$create_time', 0, 7]  
        ], 'count' => ['$sum' => 1]]],
        ['$sort' => ['_id' => 1]],
        ['$project' => ['_id' => 0, "date" => '$_id', "count" => 1]],
    ]
);


$data = [];

foreach ($cursor as $v) {
    array_push($data, $v);
}

$data = json_encode($data);

echo $data;
