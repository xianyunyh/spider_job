import { getIdByUrl } from './utils'
import { JobItem, Salary } from './job'
import { Spider } from './spider'
export default class ZhiPin extends Spider {
    async run(url: string) {
        await this.page.goto(url, { timeout: 30000, waitUntil: "domcontentloaded" })
        const resp = await this.page.goto(url)
        if (!resp) {
            return
        }
        console.log("响应code:" + resp.status() + "url" + resp.url())
        const items = await this.scrapeInfiniteScrollItems(this.extractItems, 100);
        let results = []
        for (let index = 0; index < items.length; index++) {
            let detailUrl = items[index];
            let res = await this.gotoDetail(detailUrl)
            if (res == false) {
                continue;
            }
            console.log(res)
            results.push(res)
            await this.page.waitFor(2000);
        }
        console.log("total:", results.length)
    }
    private parseSalary(salary: string): Salary {
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
    async gotoDetail(url: string): Promise<JobItem | boolean> {
        try {
            const page = this.page;
            await page.goto(url)
            await page.waitFor("body")
            const postion_id = getIdByUrl(url)
            let title = await this.getElementText("#main h1")
            let salary: string = await this.getElementText("h1 .salary")
            const position_name = title.replace(salary, "")
            let create = await this.getElementText(".time")
            const create_time = create.replace("更新于：", "")
            let vline = await page.$eval("#main > div.job-banner > p", e => e.innerHTML)
            let vlineArr = vline.split(`<em class="vline"></em>`)
            let work_year = vlineArr[1]
            if (work_year.indexOf("年") == -1) {
                work_year = "不限"
            }

            let educational = vlineArr[vlineArr.length - 1]
            let salarys = this.parseSalary(salary)
            let company_name = await this.getElementText(".business-info h4")
            let body = await page.$$eval(".job-sec .text", e => e.map(l => l.textContent).join("\n"))
            let address = await this.getElementText(".location-address")
            let gray = await page.$eval(".job-company .gray", e => e.innerHTML)
            let grayArr = gray.split(`<em class="vline"></em>`)
            let company_url = await page.$eval(".link-all", a => a.getAttribute('href')) || ''
            let company_scale = grayArr[2] || ""
            let company_stage = grayArr[1] || ""
            let company_area = grayArr[0] || ""
            let map = await page.evaluate(() => {
                const el = document.getElementById('map-container');
                let long_lat = el && el.getAttribute("data-long-lat");
                return long_lat
            });
            
            const maps = (map || '').split(",")
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
    extractItems(): Array<string> {
        return this.extractItemLinks('#main li.item a')
    }
}