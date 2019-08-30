package models

import (
	"context"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type Company struct {
	CompanyId   string `bson:"company_id" json:"company_id"`
	CompanyName string `bson:"company_name" json:"company_name"`
	CompanyScale string `bson:"company_scale" json:"company_scale"`
	CompanyArea string `bson:"company_area" json:"company_area"`
	CompanySite string `bson:"company_site" json:"company_site"`
	CompanyStage string `bson:"company_stage" json:"company_stage"`
	PositionLng string `bson:"position_lng" json:"position_lng"`
	PositionLat string `bson:"position_lat" json:"position_lat"`
	Address string `bson:"address" json:"address"`
}
func (c *Company) GetCompanies(page,limit int64) ([]Company,error) {
	filter := bson.D{
		{"_id",0},
		{"$comment",bson.M{"$slice":[]int{20,10}}},
	}
	option := options.Find().SetProjection(filter)
	skip := (page-1) * limit
	option.Limit = &limit
	option.Skip = &skip
	cur, err := Db.Collection("company").Find(context.TODO(), bson.M{}, option)
	if err != nil {
		return nil,err
	}
	result := make([]Company, 0)
	err = cur.All(context.TODO(), &result)
	if err != nil {
		return nil,err
	}
	return result,nil
}

func (c *Company) GetCompanyAny(group string) ([]map[string]interface{},error) {
	pipe := bson.A{
		bson.M{
			"$group":bson.M{
				"_id":"$"+group,
				"total":bson.M{
					"$sum": 1,
				},
			},
		},
		bson.M{
			"$sort":bson.M{
				"total":-1,
			},
		},
	}
	cur,err := Db.Collection("company").Aggregate(context.TODO(),pipe)
	if err != nil{
		return nil,err
	}
	result := make([]map[string]interface{},0)
	err = cur.All(context.TODO(),&result)
	if err != nil{
		return nil,err
	}
	return result,nil
}