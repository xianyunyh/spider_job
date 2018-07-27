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
            '_id' => '$company_name',
            'count' => ['$sum' => 1],
            'postion_id' => ['$first' => '$postion_id'],
            'salary' => ['$first' => '$salary'],
        ],
        ],
        ['$sort' => ['count' => -1]],
        ['$limit' => 20],
        ['$project' =>
            [
                '_id' => 0,
                "company_name" => '$_id',
                "count" => 1,
                'postion_id' => 1,
                'salary' => 1,
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
