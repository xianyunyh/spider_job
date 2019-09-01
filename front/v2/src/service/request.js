var Fly=require("flyio/dist/npm/fly")
const base_url = process.env["NODE_ENV"] == "production" ? "http://yehe.37he.cn/v2/" : 'http://localhost:8080/v2'
const request = new Fly()
request.config.timeout=5000;
request.config.baseURL = base_url
request.interceptors.request.use((request) => {
  request.headers["v"]="2.0";
  return request
})

request.interceptors.response.use(
    (response, promise) => {
      if (response.status !== 200 ) {
        alert(response.data.message)
      }
      return promise.resolve((response.data))
    },
    (err, promise) => {
      alert("请求遇到了错误")
        return promise.reject(err)
    }
)

export default request