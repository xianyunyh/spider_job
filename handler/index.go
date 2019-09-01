package handler

import (
	"app/lib"
	"app/models"
	"context"
	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/bson"
	"log"
	"net/http"
	"strconv"
	"time"
)

func GetContext() context.Context {
	ctx, _ := context.WithTimeout(context.Background(), time.Second*5)
	return ctx
}

//var DefaultServerErr = errors.New("服务器出错")
func Index(c *gin.Context) {
	r, _ := models.Db.Collection("position").Distinct(context.TODO(), "company_name", bson.D{})
	c.JSON(200, r)
	return
}

func CompanyList(c *gin.Context) {
	company := &models.Company{}
	pageNum := c.DefaultQuery("page", "1")
	pageSize := c.DefaultQuery("page_size", "10")
	page, _ := strconv.Atoi(pageNum)
	limit, _ := strconv.Atoi(pageSize)
	data, err := company.GetCompanies(int64(page), int64(limit))
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}
	c.JSON(http.StatusOK, data)
}
func CompanyAnaly(c *gin.Context) {
	company := &models.Company{}
	groups := []string{"company_stage", "company_scale", "company_area"}
	group := c.DefaultQuery("group", "company_scale")
	if !lib.InArray(group, groups) {
		group = "company_scale"
	}
	data, err := company.GetCompanyAny(group)
	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	c.JSON(http.StatusOK, data)
}
func WorkYear(c *gin.Context) {
	data, err := models.GetWordYearData()
	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	c.JSON(http.StatusOK, data)
}

func Educational(c *gin.Context) {
	data, err := models.GetEducation()
	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	c.JSON(http.StatusOK, data)
}

func Weekly(c *gin.Context) {
	data, err := models.GetWeeklyData()
	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	c.JSON(http.StatusOK, data)
}

func Monthly(c *gin.Context) {
	data, err := models.GetMonthlyData()
	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{"message": err.Error()})
		return
	}
	c.JSON(http.StatusOK, data)
}

func CompanyJobs(c *gin.Context) {
	companyId := c.Param("company_id")
	c.JSON(http.StatusOK, models.GetJobsByCompany(companyId))
}
func GetHotCompany(c *gin.Context) {
	c.JSON(http.StatusOK, models.GetHotCompany())
}

func AddCompany(c *gin.Context) {
	body := make([]models.Company, 0)
	err := c.BindJSON(&body)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	for _, item := range body {
		count, err := models.Db.Collection("company").CountDocuments(GetContext(), bson.M{"company_id": item.CompanyId})
		if err != nil || count > 0 {
			log.Println(err)
			continue
		}
		ins, err := models.Db.Collection("company").InsertOne(GetContext(), item)
		if err != nil {
			log.Println(err)
			continue
		}
		log.Println(ins.InsertedID)
	}
	c.JSON(http.StatusOK, gin.H{"message": "ok"})
}

func AddPosition(c *gin.Context) {
	positions := make([]models.Position, 0)
	err := c.BindJSON(&positions)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"message": err.Error()})
		return
	}

	for _,position := range positions {
		filter := bson.M{
			"postion_id":position.PositionId,"create_time":position.CreateTime,
		}
		count, err := models.Db.Collection("position").CountDocuments(context.Background(),filter)
		if err != nil && count >= 1 {
			continue;
		}
		ins ,err := models.Db.Collection("position").InsertOne(context.TODO(),position)
		if err != nil {
			continue
		}
		log.Println(ins.InsertedID)
	}
	c.JSON(http.StatusOK,gin.H{})
}
