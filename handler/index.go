package handler

import (
	"app/models"
	"github.com/gin-gonic/gin"
	"net/http"
	"app/lib"
	"strconv"
)

//var DefaultServerErr = errors.New("服务器出错")
func Index(c *gin.Context) {

}
func CompanyList(c *gin.Context)  {
	company := &models.Company{}
	pageNum := c.DefaultQuery("page","1")
	pageSize := c.DefaultQuery("page_size","10")
	page,_ := strconv.Atoi(pageNum)
	limit,_ := strconv.Atoi(pageSize)
	data,err := company.GetCompanies(int64(page),int64(limit))
	if err != nil {
		c.JSON(http.StatusInternalServerError,gin.H{"message":err.Error()})
		return
	}
	c.JSON(http.StatusOK,data)
}
func CompanyAnaly(c *gin.Context)  {
	company := &models.Company{}
	groups := []string{"company_stage","company_scale","company_area"}
	group := c.DefaultQuery("group", "company_scale")
	if !lib.InArray(group,groups) {
		group = "company_scale"
	}
	data,err := company.GetCompanyAny(group)
	if err != nil {
		c.JSON(http.StatusBadGateway,gin.H{"message":err.Error()})
		return
	}
	c.JSON(http.StatusOK,data)
}
func WeeklyData(c *gin.Context)  {
	data,err := models.GetWeeklyData()
	if err != nil {
		c.JSON(http.StatusBadGateway,gin.H{"message":err.Error()})
		return
	}
	c.JSON(http.StatusOK,data)
}