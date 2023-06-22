import { Page } from 'puppeteer'
import type { JobItem, Salary } from '../types/job'
import type { ZhiPinConfig } from '../types'
import { extractItemLinks, getIdByUrl, getElementText,sleep} from '../utils'

export const run = async (page: Page, conf: ZhiPinConfig) => {
    const { start_url, city_code, position } = conf
    const url = start_url + `?query=&city=${city_code}&position=${position}`
    await page.goto(url, { timeout: 30000, waitUntil: "domcontentloaded" })
    const resp = await page.goto(url)
    if (!resp) {
        return
    }
    console.log("响应code:" + resp.status() + "url" + resp.url())
    await page.waitForSelector(".job-list-box .job-card-left",{timeout: 10000})
    const items = await page.evaluate(extractItemLinks, ".job-list-box .job-card-left") as Array<string>;
    let results = []
    for (let index = 0; index < 10; index++) {
        let detailUrl = 'https://www.zhipin.com' + items[index].trim();
        const res = await gotoDetail(page, detailUrl)
        console.log(detailUrl)
        // let res = false
        if (index == 4) {
            break;
        }
        console.log(res)
        await sleep(5000)
    }
    console.log("total:", results.length)
}

const gotoDetail = async (page: Page, url: string): Promise<JobItem | boolean> => {
    try {
        await page.goto(url)
        await page.waitForSelector("h1")
        const postion_id = getIdByUrl(url)
        let title = await getElementText(page, "h1")
        let salary: string = await getElementText(page, ".info-primary .salary")
        const position_name = title.replace(salary, "")
        let create = await getElementText(page, ".time")
        const create_time = create.replace("更新于：", "")
        let work_year = await getElementText(page,".text-experiece")
        if (work_year.indexOf("年") == -1) {
            work_year = "不限"
        }

        let educational = await getElementText(page,".text-degree")
        let salarys = parseSalary(salary)
        let company_name = await getElementText(page, ".business-info-box .company-name")
        let body = await getElementText(page, ".job-sec-text")
        let address = await getElementText(page, ".location-address")
        let grayArr = await page.evaluate(() => {
            let items: Array<string> = []
            document.querySelectorAll(".sider-company > p").forEach((e) => {
                items.push((e.textContent || '').trim())
            })
            return items;
        });
        let company_url = await page.$eval(".business-info-box a", a => a.getAttribute('href')) || ''
        let company_stage = grayArr[1] || ""//发展阶段   
        let company_scale = grayArr[2] || ""
        let company_area = grayArr[3] || ""
        let map = await page.evaluate(() => {
            const el = document.querySelector('.job-location-map');
            let long_lat = el && el.getAttribute("data-lat");
            return long_lat
        });

        const maps = (map || '').split(",")
        company_name  = company_name.replace("公司名称","")
        let company_info = {
            company_id: getIdByUrl(company_url),
            company_name: company_name.replace(/\s+/g, ""),
            company_scale: company_scale.replace(/\s+/g, ""),//公司规模
            company_stage: company_stage.replace(/\s+/g, ""), //发展阶段
            company_area: company_area.replace(/\s+/g, ""),//公司领域
            company_site: company_url,//公司网站
            position_lng: maps[0],
            position_lat: maps[1],
        }
        return {
            address,
            salary: salarys,
            create_time,
            body,
            company_name,
            postion_id,
            position_name,
            educational,
            work_year,
            from_site: "ZhiPin",
            company_info
        }

    } catch (error) {
        console.log(error)
        return false
    }
}
const parseSalary = (salary: string): Salary => {
    let temp = {
        min: 0,
        max: 0,
        avg: 0
    }
    //s = "13-22K·13薪"
    salary = salary || ""
    if (salary.length == 0) {
        return temp
    }
    const t = salary.split("·")[0].split("-")
    if (t.length < 2) {
        return temp
    }
    let [min, max] = t
    let step = 1
    if (max.indexOf("万") > 0 || max.indexOf("W") > 0) {
        step = 10000
    } else if (max.indexOf("千") > 0 || max.indexOf("K") > 0) {
        step = 1000
    }
    temp.min = parseFloat(min) * step
    temp.max = parseFloat(max) * step
    temp.avg = Number((temp.min + temp.max) / 2)
    return temp
}
export default { run };