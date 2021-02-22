import Url from 'url-parse'
import dayjs from 'dayjs';

export function getIdByUrl(url: string ): string {
    let uParse = new Url(url)
    let path = uParse.pathname
    const pathArr = path.split("/")
    return pathArr[pathArr.length - 1].replace(".html", "")
}

export function parseEdu(edu: string) {
    const edus = ["大专", "本科", "硕士", "博士", "不限"]
    for (let element of edus) {
        if (edu.indexOf(element) >= 0) {
            return element
        }
    }
    return "不限"
}
export function parseWorkYear(w: string) {
    const wks = ["毕业生", "1-3年", "3-5年", "5-10年", "10年以上", "经验不限"]
    for (let element of wks) {
        if (w.indexOf(element) >= 0) {
            return element
        }
    }
    return "经验不限"
}

export function  parseLaGouTime(t: string) {
    if (t.length == 0) {
        return ""
    }
    if (t.indexOf(":") >= 0) {
        return dayjs().format("YYYY-MM-DD")
    }
    let reg = t.match(/(\d+)天前/i)
    if (reg) {
        return dayjs().subtract(Number(reg[1]), 'day').format("YYYY-MM-DD")
    }
    if (/\d{4}\-\d{2}\-\d{2}/.test(t)) {
        return t
    }
    return ""
}