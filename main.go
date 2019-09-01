package main

import (
	"app/config"
	"app/handler"
	"app/models"
	"encoding/json"
	"github.com/gin-gonic/gin"
	"github.com/gin-contrib/cors"
	"io/ioutil"
	"log"
	"strconv"
	"time"
)
const (
	APIVersion = "v2"
)
func SetCors(app *gin.Engine)  {
	app.Use(cors.New(cors.Config{
		AllowOrigins:     []string{"*"},
		AllowMethods:     []string{"PUT","GET","POST","OPTIONS"},
		AllowHeaders:     []string{"Origin","content-type","v"},
		ExposeHeaders:    []string{"Content-Length","content-type","v"},
		AllowCredentials: true,
		MaxAge: 12 * time.Hour,
	}))
}

func AddRouter(router *gin.Engine)  {
	g := router.Group("/" + APIVersion)
	g.Any("/", handler.Index)
	g.GET("/company",handler.CompanyList)
	g.POST("/company",handler.AddCompany)
	g.POST("/position",handler.AddPosition)
	g.GET("/company/hot",handler.GetHotCompany)
	g.GET("/company/job/:company_id",handler.CompanyJobs)
	g.GET("/company/analysis",handler.CompanyAnaly)
	g.GET("/position/work_year",handler.WorkYear)
	g.GET("/position/edu",handler.Educational)
	g.GET("/position/weekly",handler.Weekly)
	g.GET("/position/monthly",handler.Monthly)
	g.GET("/word", func(c *gin.Context) {
		data,_ := ioutil.ReadFile("./word.json")
		result := make(map[string]interface{},0)
		_ = json.Unmarshal(data,&result)
		c.JSON(200,result)
	})
}

func Run()  {
	gin.SetMode(gin.ReleaseMode)
	router := gin.Default()
	SetCors(router)
	AddRouter(router)
	log.Fatal(router.Run(config.Conf.Ip + ":"+strconv.Itoa(config.Conf.Port)))
}
func main()  {
	//初始化配置
	err := config.Init("./config.json")
	if err != nil {
		log.Fatal(err)
	}
	models.Init()
	Run()
}
