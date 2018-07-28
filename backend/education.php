<?php
require './vendor/autoload.php';
header("Content-Type: application/json;charset=utf-8");
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Origin: *');
$client = new MongoDB\Client("mongodb://127.0.0.1");

$collection = $client->job->position;

$cursor = $collection->aggregate(
    [
        ['$group' => [
            '_id' => '$educational',
            'count' => ['$sum' => 1],
            'salary' => ['$avg' => '$salary.avg'],
        ],

        ],
        ['$sort' => ['salary' => 1]],
        ['$project' =>
            [
                '_id' => 0,
                "educational" => '$_id',
                "count" => 1,
                "salary" => 1,
            ],
        ],
    ]
);

$data = [];

foreach ($cursor as $v) {
    array_push($data, $v);
}

$data = json_encode($data);

echo $data;
exit();
