package main

import (
	"app/config"
	"app/models"
	"github.com/gin-gonic/gin"
	"log"
	"strconv"
	"app/handler"
)

func main()  {
	//初始化配置
	err := config.Init("./config.json")
	if err != nil {
		log.Fatal(err)
	}
	models.Init()
	gin.SetMode(gin.ReleaseMode)
	router := gin.Default()
	router.Any("/", handler.Index)
	router.GET("/company",handler.CompanyList)
	router.GET("/company/analysis",handler.CompanyAnaly)
	router.GET("/position/weekly",handler.WeeklyData)
	router.GET("/ping", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	log.Println(config.Conf.Port)
	router.Run(config.Conf.Ip + ":"+strconv.Itoa(config.Conf.Port))
}
