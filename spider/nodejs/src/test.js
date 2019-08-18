const dayjs = require("dayjs")
function parseTime(t) {
    if(t.indexOf(":")>= 0) {
        return dayjs().format("YYYY-MM-DD")
    }
    if(reg = t.match(/(\d+)天前/i)) {
        return dayjs().subtract(reg[1], 'day').format("YYYY-MM-DD")
    }
    if(/\d{4}\-\d{2}\-\d{2}/.test(t)) {
        return t
    }
    return ""
}
function parseEdu(edu) {
    const edus = ["大专","本科","硕士","博士","不限"]
    for (let element of edus) {
        if (edu.indexOf(element) >=0 ) {
            return element
        }
      }
      return "不限"
}
function parseWorkYear(edu) {
    const edus = ["毕业生","1-3年","3-5年","5-10年","10年以上","经验不限"]
    for (let element of edus) {
        if (edu.indexOf(element) >=0 ) {
            return element
        }
      }
      return "经验不限"
}
console.log(parseWorkYear("经验1-3年"))
console.log(parseWorkYear("经验应届毕业生"))
console.log(parseWorkYear("经验3-5年"))
console.log(parseWorkYear("经验5-10年"))
console.log(parseWorkYear("经验10年以上"))
