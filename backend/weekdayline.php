<?php
require './vendor/autoload.php';
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Origin: *');
$client = new MongoDB\Client("mongodb://127.0.0.1");

$collection = $client->job->position;

$today = date("Y-m-d");
$beforeWeek = date("Y-m-d", strtotime("-7 day"));
$where = [
    "create_time" => [
        '$gt' => "2018-07-24",
    ],
];
$cursor = $collection->aggregate(
    [
        ['$match' => ['create_time' => ['$gte' => $beforeWeek, '$lte' => $today]]],
        ['$group' => ['_id' => '$create_time', 'count' => ['$sum' => 1]]],
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
