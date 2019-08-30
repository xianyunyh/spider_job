package models

import (
	"context"
	"go.mongodb.org/mongo-driver/bson"
	"log"
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
// 获取周线
func GetWeeklyData()([]map[string]interface{},error)  {
	pipe := bson.A{
		bson.M{
			"$group":bson.M{
				"_id":"$work_year",
				"count":bson.M{
					"$sum": 1,
				},
				"salary":bson.M{
					"$avg":"$salary.avg",
				},
			},
		},
		bson.M{
			"$sort":bson.M{
				"salary":1,
			},
		},
		bson.M{
			"$project":bson.D{
				{"_id",0},
				{"work_year","$_id"},
				{"count",1},
				{"salary",bson.M{
					"$toInt":"$salary",
				}},
			},
		},
	}
	cur,err := Db.Collection("position").Aggregate(context.Background(),pipe)
	if err != nil {
		return nil,err
	}
	result := make([]map[string]interface{},0)
	log.Println(err)
	err = cur.All(context.Background(),&result)
	if err != nil {
		return nil,err
	}
	return result,nil
}
