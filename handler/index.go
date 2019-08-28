package handler

import (
	"app/models"
	"context"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/bson"
	"log"
	"time"
)

func Index(c *gin.Context) {
	ctx,cancel := context.WithTimeout(context.TODO(),time.Second * 10)
	defer cancel()
	s,err := models.Db.Collection("company").Find(ctx,bson.D{})
	if err != nil {
		c.JSON(500,err)
		return
	}
	r := make(map[string]interface{})
	err = s.Decode(&r)
	if err != nil {
		c.JSON(500,err)
		return
	}
	log.Println(r)
	c.JSON(200,r)
}
