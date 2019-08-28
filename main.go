package main

import (
	"app/config"
	"app/models"
	"github.com/gin-gonic/gin"
	"log"
)

func main()  {
	//初始化配置
	err := config.Init("./config.json")
	if err != nil {
		log.Fatal(err)
	}
	models.Init()
	log.Println()
	r := gin.Default()
	Router(r)
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	log.Fatal(r.Run())
}
