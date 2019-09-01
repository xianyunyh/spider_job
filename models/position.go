package models

import (
	"context"
	"go.mongodb.org/mongo-driver/bson"
	"log"
	"time"
)

type SalaryRange struct {
	Max int `bson:"max" json:"max"`
	Min int `bson:"min" json:"min"`
	Avg int `bson:"avg" json:"avg"`
}
type Position struct {
	PositionId     string      `bson:"postion_id" json:"postion_id"`
	PositionName   string      `bson:"position_name" json:"position_name"`
	Educational    string      `bson:"educational" json:"educational"`
	CreateTime     string      `bson:"create_time" json:"create_time"`
	JobDescription string      `bson:"body" json:"body"`
	CompanyName    string      `bson:"company_name" json:"company_name"`
	CompanyId      string      `bson:"company_id" json:"company_id"`
	WorkYear       string      `bson:"work_year" json:"work_year"`
	Salary         SalaryRange `bson:"salary" json:"salary"`
}

func getContext() context.Context {
	ctx,cancel := context.WithTimeout(context.Background(),time.Second * 3)
	defer cancel()
	return ctx
}
// 获取周线
func GetWordYearData() ([]map[string]interface{}, error) {
	pipe := bson.A{
		bson.M{
			"$group": bson.M{
				"_id": "$work_year",
				"count": bson.M{
					"$sum": 1,
				},
				"salary": bson.M{
					"$avg": "$salary.avg",
				},
			},
		},
		bson.M{
			"$sort": bson.M{
				"salary": 1,
			},
		},
		bson.M{
			"$project": bson.D{
				{"_id", 0},
				{"work_year", "$_id"},
				{"count", 1},
				{"salary", bson.M{
					"$toInt": "$salary",
				}},
			},
		},
	}
	cur, err := Db.Collection("position").Aggregate(context.Background(), pipe)
	if err != nil {
		return nil, err
	}
	result := make([]map[string]interface{}, 0)
	log.Println(err)
	err = cur.All(context.Background(), &result)
	if err != nil {
		return nil, err
	}
	return result, nil
}

func GetEducation() ([]map[string]interface{}, error) {
	pipe := bson.A{
		bson.M{
			"$group": bson.M{
				"_id": "$educational",
				"count": bson.M{
					"$sum": 1,
				},
				"salary": bson.M{
					"$avg": "$salary.avg",
				},
			},
		},
		bson.M{
			"$sort": bson.M{
				"salary": 1,
			},
		},
		bson.M{
			"$project": bson.D{
				{"_id", 0},
				{"educational", "$_id"},
				{"count", 1},
				{"salary", bson.M{
					"$toInt": "$salary",
				}},
			},
		},
	}
	cur, err := Db.Collection("position").Aggregate(context.Background(), pipe)
	if err != nil {
		return nil, err
	}
	result := make([]map[string]interface{}, 0)
	log.Println(err)
	err = cur.All(context.Background(), &result)
	if err != nil {
		return nil, err
	}
	return result, nil
}

func GetMonthlyData ()([]map[string]interface{}, error)  {
	end := time.Now()
	begin := end.AddDate(0,-6,0)
	group := bson.M{
		"_id":bson.M{
			"$substr":bson.A{
				"$create_time",0,7,
			},
		},
		"count":bson.M{
			"$sum":1,
		},
	}
	return GetGroupData(group,begin,end)
}
func GetWeeklyData() ([]map[string]interface{}, error) {
	end := time.Now()
	begin := end.Add(-7*24*time.Hour)
	group := bson.M{
		"_id":"$create_time",
		"count":bson.M{
			"$sum":1,
		},
	}
	return GetGroupData(group,begin,end)
}
func GetGroupData(group bson.M,begin,end time.Time) ([]map[string]interface{}, error) {

	pipe := bson.A{
		bson.M{
			"$match":bson.M{
				"create_time":bson.M{
					"$gte":begin.Format("2006-01-02"),
					"$lte":end.Format("2006-01-02"),
				},
			},
		},
		bson.M{
			"$group": group,
		},
		bson.M{
			"$sort": bson.M{
				"_id": 1,
			},
		},
		bson.M{
			"$project": bson.D{
				{"_id", 0},
				{"date", "$_id"},
				{"count", 1},
			},
		},
	}
	cur, err := Db.Collection("position").Aggregate(context.Background(), pipe)
	if err != nil {
		return nil, err
	}
	result := make([]map[string]interface{}, 0)
	log.Println(err)
	err = cur.All(context.Background(), &result)
	if err != nil {
		return nil, err
	}
	return result, nil
}

func GetJobsByCompany(company_id string)[]Position  {
	filter := bson.D{
		{"company_id",company_id},
	}
	//findOption := options.Find()
	//findOption.set
	cur,_ := Db.Collection("position").Find(context.TODO(),filter)
	result := make([]Position,0)
	_ = cur.All(context.TODO(),&result)
	return result
}

func GetHotCompany () ([]map[string]interface{})  {
	pipe := bson.A{
		bson.M{
			"$match":bson.M{
				"create_time":bson.M{
					"$gte":"2019-01-01",
					"$lte":"2019-10-01",
				},
				"company_id":bson.M{
					"$exists":true,
					"$ne":"",
				},
			},
		},
		bson.M{
			"$group": bson.M{
				"_id":"$company_id",
				"count":bson.M{
					"$sum":1,
				},
				"postion_id":bson.M{
					"$first":"$postion_id",
				},
				"salary":bson.M{
					"$first":"$salary",
				},
				"company_name":bson.M{
					"$first":"$company_name",
				},
			},
		},
		bson.M{
			"$sort": bson.M{
				"count": -1,
			},
		},
		bson.M{
			"$limit": 20,
		},
		bson.M{
			"$project": bson.D{
				{"_id", 0},
				{"company_name", 1},
				{"company_id", "$_id"},
				{"count", 1},
				{"salary", 1},
			},
		},
	}
	cur,_ := Db.Collection("position").Aggregate(context.Background(),pipe)
	result := make([]map[string]interface{}, 0)
	err := cur.All(context.TODO(),&result)
	if err != nil {
		log.Println(err)
	}
	return result
}