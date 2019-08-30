module app

go 1.12

require (
	github.com/gin-gonic/gin v1.4.0
	github.com/go-stack/stack v1.8.0 // indirect
	github.com/golang/snappy v0.0.1 // indirect
	github.com/google/go-cmp v0.3.1 // indirect
	github.com/tidwall/pretty v1.0.0 // indirect
	github.com/xdg/scram v0.0.0-20180814205039-7eeb5667e42c // indirect
	github.com/xdg/stringprep v1.0.0 // indirect
	go.mongodb.org/mongo-driver v1.1.0
	golang.org/x/sync v0.0.0-20190423024810-112230192c58 // indirect
)

replace go.mongodb.org/mongo-driver v1.1.0 => github.com/mongodb/mongo-go-driver v1.1.0
