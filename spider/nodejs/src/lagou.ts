import { EvaluateFn } from 'puppeteer'
import { JobItem, Salary } from './job';
import { Spider } from './spider';
import { getIdByUrl, parseEdu, parseWorkYear, parseLaGouTime } from "./utils";

export default class Lagou extends Spider {
    async run(url: string) {
        try {
            await this.page.goto(url)
            let items = await this.getListItems(this.extractItems, 40, 5000) || []

            for (let index = 0; index < items.length; index++) {
                let url = items[index];
                let res = await this.gotoDetail(url)
                if (res === false) {
                    continue;
                }
                console.log(res)
                await this.page.waitFor(2000);
            }
        } catch (e) {
            console.log(e)
            //process.exit(1)
        }
    }
    async getList(url: string) {
        try {
            const resp = await this.page.goto(url);
            await this.page.waitFor(1000)
            // $ = cheerio.load(resp.text)
            // return $(".item a").each(function (e) {
            //     return e.href
            // })
        } catch (e) {
            return false;
        }
    }
    extractItems(): Array<string> {
        return this.extractItemLinks('.s_position_list  .item_con_list li .position a')
    }
    async getListItems(
        extractItems: EvaluateFn,
        itemTargetCount: number,
        scrollDelay: number = 1000,
    ) {
        const page = this.page;
        try {
            let items: Array<string> = await page.evaluate(extractItems) || [];
            while (items.length < itemTargetCount) {
                await page.click(".pager_container .pager_next", { delay: 500 })
                let temp: Array<string> = await page.evaluate(extractItems);
                items = [...items, ...temp]
                await page.waitFor(scrollDelay);
            }
            return items;
        } catch (e) {
            console.log(e.message)
            return false;
        }

    }
    parseSalary(salary: string): Salary {
        let temp = {
            min: 0,
            max: 0,
            avg: 0
        }
        salary = salary || ""
        if (salary.length == 0) {
            return temp
        }
        let t = salary.split("·")[0].split("-")
        if (t.length < 2) {
            return temp
        }
        let [min, max] = t
        const parseMoney = (m: string) => {
            let step = 1
            m = m.toLocaleUpperCase()
            if (m.indexOf("W") > 0) {
                m = m.replace("W", "")
                step = 10000
            } else if (m.indexOf("K") > 0) {
                m = m.replace("K", "")
                step = 1000
            }
            return parseFloat(m) * step
        }

        temp.min = parseMoney(min)
        temp.max = parseMoney(max)
        temp.avg = Number((temp.min + temp.max) / 2)
        return temp
    }

    async gotoDetail(url: string): Promise<JobItem|false> {
        const page = this.page;
        try {
            await page.goto(url)
            await page.waitForSelector("body")
            const postion_id = getIdByUrl(url)
            let title = await this.getElementText("h2.name")
            let salary = await this.getElementText(".salary")
            let create = await this.getElementText(".publish_time")
            let work_year = await this.getElementText(".job_request span:nth-child(3)")
            let educational = await this.getElementText(".job_request span:nth-child(4)");
            let company_name = await this.getElementText(".job_company_content .fl-cn") || '';
            let body = await this.getElementText(".job-detail")
            let address = await this.getElementText(".work_addr")
            let company_url = await page.$eval("#job_company > dt > a", a => a.getAttribute("href") || '')
            let company_scale = await this.getElementText("#job_company > dd > ul > li:nth-last-child(2)  h4")
            let company_stage = await this.getElementText("#job_company > dd > ul > li:nth-child(2)  h4")
            let company_area = await this.getElementText("#job_company > dd > ul > li:nth-child(1)  h4")
            let company_site = await page.$eval("#job_company > dd > ul > li:nth-last-child(1)  a", a => a.getAttribute("href") || '')
            let company_info = {
                company_id: getIdByUrl(company_url),
                company_name: company_name.replace(/\s+/g, ""),
                company_scale: company_scale,//公司规模
                company_stage: company_stage, //发展阶段
                company_area: company_area,//公司领域
                company_site: company_site,//公司网站
                position_lng: await page.$eval("input[name=positionLng]", input => input.getAttribute("value") || ''),
                position_lat: await page.$eval("input[name=positionLat]", input => input.getAttribute("value") || ''),
            }
            return {
                postion_id,
                body,
                address: address.replace("查看地图", "").replace(/\s+/g, ""),
                salary: this.parseSalary(salary),
                create_time: parseLaGouTime(create.replace("发布于拉勾网", "")),
                company_name: company_name.replace(/\s+/g, ""),
                position_name: title.replace(salary, ""),
                educational: parseEdu(educational),
                work_year: parseWorkYear(work_year),
                from_site: "lagou",
                company_info,
            }

        } catch (error) {
            console.log(error)
            return false;
        }
    }
}