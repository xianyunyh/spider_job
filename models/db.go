package models

import (
	"app/config"
	"context"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"sync"
	"time"
)

type MongoClient struct {
	Client *mongo.Client
	Ctx    context.Context
}

var Mongo *MongoClient
var Db 	  *mongo.Database
//初始化
func Init() {
	var once sync.Once
	once.Do(func() {
		ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
		defer cancel()
		if client, err := mongo.Connect(ctx, options.Client().ApplyURI(config.Conf.MgoUri)); err == nil {
			Mongo = &MongoClient{}
			Mongo.Ctx = ctx
			Mongo.Client = client
			Db = Mongo.Client.Database(config.Conf.Database)
		}
	})
}
