package main

import (
	. "app/handler"
	"github.com/gin-gonic/gin"
)

func Router(router *gin.Engine)  {
	router.GET("/someGet",Index )
}
