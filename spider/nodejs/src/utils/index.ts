import Url from 'url-parse'
import dayjs from 'dayjs';
import {Page} from 'puppeteer'
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
export const  extractItemLinks = (selector: string): Array<string> => {
    const extractedElements = document.querySelectorAll(selector);
    let items: Array<string> = [];
    extractedElements.forEach(element => {
        items.push(element.getAttribute("href") || '')
    })
    return items;
}

export const getElementText = async (page: Page,selector: string): Promise<string> =>{
    try {
        await page.waitForSelector(selector);
        return await page.$eval(selector, ele => ele.textContent || '');
    } catch (e) {
        return "";
    }
}

export function sleep(ms: number) {
    return new Promise(resolve=>setTimeout(resolve, ms))
}