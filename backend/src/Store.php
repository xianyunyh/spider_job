<?php

namespace Boss;

class Store
{
    /**
     * @var \MongoDB\Collection
     */
    private $collection;

    public function __construct(array $config = [])
    {
        try {
            $uri    = $config["uri"] ?? "mongodb://127.0.0.1";
            $client = new MongoDB\Client($uri);
            if (!isset($config['db']) || empty($config['db'])) {
                throw new Exception("没设置db");
            }
            if (!isset($config['collection']) || empty($config['collection'])) {
                throw new Exception("没设置collection");
            }
            $this->collection = $client->{$config['db']}->{$config['collection']};
        } catch (\Exception $e) {
            throw new Exception($e->getMessage());
        }
    }

    /**
     * 获取热门公司
     * @return array
     */
    public function getHostCompany(DateTimeImmutable $startDate, DateTimeImmutable $end)
    {
        $cursor = $this->collection->aggregate(
            [
                ['$group' => [
                    '_id' => '$company_name',
                    'count' => ['$sum' => 1],
                    'postion_id' => ['$first' => '$postion_id'],
                    'salary' => ['$first' => '$salary'],
                ],
                ],
                ['$match' => ['create_time' => ['$gte' => $startDate->format("Y-m-d"), '$lte' => $end->format("Y-m-d")]]],
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
        return iterator_to_array($cursor, true);
    }

    /**
     * 工作年限情况
     */
    public function getWorkYear(DateTimeImmutable $startDate, DateTimeImmutable $endDate)
    {
        $cursor = $this->collection->aggregate(
            [
                ['$group' => [
                    '_id' => '$work_year',
                    'count' => ['$sum' => 1],
                    'salary' => ['$avg' => '$salary.avg'],
                ],
                ],
                ['$sort' => ['salary' => 1]],
                ['$match' => [
                    'create_time' => [
                        '$gte' => $startDate->format("Y-m-d"),
                        '$lte' => $endDate->format("Y-m-d")]]
                ],
                ['$project' =>
                    [
                        '_id' => 0,
                        "work_year" => '$_id',
                        "count" => 1,
                        "salary" => 1,
                    ],
                ],
            ]
        );
        return iterator_to_array($cursor, true);
    }

    /**
     * 教育情况
     * @return array
     */
    public function getEdu(DateTimeImmutable $startDate, DateTimeImmutable $endDate)
    {
        $cursor = $this->collection->aggregate(
            [
                ['$group' => [
                    '_id' => '$educational',
                    'count' => ['$sum' => 1],
                    'salary' => ['$avg' => '$salary.avg'],
                ],
                ],
                ['$sort' => ['salary' => 1]],
                ['$match' => [
                    'create_time' => [
                        '$gte' => $startDate->format("Y-m-d"),
                        '$lte' => $endDate->format("Y-m-d")]]
                ],
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
        return iterator_to_array($cursor, true);
    }

    /**
     * 按周统计
     * @return array
     */
    public function getWeekLine(DateTimeImmutable $startDate, DateTimeImmutable $endDate)
    {
        return $this->getGroupData($startDate, $endDate, '$create_time');
    }

    /**
     * 按月统计
     */
    public function getMonthlyData(DateTimeImmutable $startDate, DateTimeImmutable $endDate)
    {
        return $this->getGroupData($startDate, $endDate, ['$substr' => ['$create_time', 0, 7]]);
    }

    /**
     * 获取分组数据
     * @param DateTimeImmutable $startDate
     * @param DateTimeImmutable $endDate
     * @param $groupId 分组
     * @return array
     */
    public function getGroupData(DateTimeImmutable $startDate, DateTimeImmutable $endDate, $groupId)
    {
        $cursor = $this->collection->aggregate(
            [
                ['$match' => ['create_time' => ['$gte' => $startDate->format("Y-m-d"), '$lte' => $endDate->format("Y-m-d")]]],
                ['$group' => ['_id' => $groupId, 'count' => ['$sum' => 1]]],
                ['$sort' => ['_id' => 1]],
                ['$project' => ['_id' => 0, "date" => '$_id', "count" => 1]],
            ]
        );
        return iterator_to_array($cursor);

    }

    public function __destruct()
    {
        unset($this->collection);
    }
}