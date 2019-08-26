const spider = require('../lib/spider');
const axios = require("axios")
const Url = require('url-parse');

function extractItems() {
    const extractedElements = document.querySelectorAll('#main li.item a');
    const items = [];
    for (let element of extractedElements) {
        items.push(element.href);
    }
    return items;
}

async function scrapeInfiniteScrollItems(
    page,
    extractItems,
    itemTargetCount,
    scrollDelay = 1000,
) {
    let items = [];
    try {
        let previousHeight;
        while (items.length < itemTargetCount) {
            items = await page.evaluate(extractItems);
            previousHeight = await page.evaluate('document.body.scrollHeight');
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)');
            await page.waitForFunction(`document.body.scrollHeight > ${previousHeight}`);
            await page.waitFor(scrollDelay);
        }
    } catch (e) {
        console.log(e)
        return false;
    }
    return items;
}
async function getElementText(page, selector) {
    try {
        await page.waitForSelector(selector);
        return await page.$eval(selector, ele => ele.textContent);
    } catch (e) {
        console.log(e)
        return "";
    }
}
function getIdByUrl(url) {
    let uParse = new Url(url)
    let path = uParse.pathname
    pathArr = path.split("/")
    return pathArr[pathArr.length - 1].replace(".html", "")
}

function parseSalary(salary) {
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
    t = salary.split("·")[0].split("-")
    if (t.length < 2) {
        return temp
    }
    let [min, max] = t
    step = 1
    if (max.indexOf("万") > 0 || max.indexOf("W") > 0) {
        step = 10000
    } else if (max.indexOf("千") > 0 || max.indexOf("K") > 0) {
        step = 1000
    }
    temp.min = parseFloat(min) * step
    temp.max = parseFloat(max) * step
    temp.avg = parseInt((temp.min + temp.max) / 2)
    return temp
}
async function gotoDetail(page, url) {
    try {
        //console.log(url)
        await page.goto(url)
        await page.waitFor("body")
        let uParse = new Url(url)
        let path = uParse.pathname
        pathArr = path.split("/")
        postion_id = pathArr[pathArr.length - 1].replace(".html", "")
        let title = await getElementText(page, "#main h1")
        let salary = await getElementText(page, "h1 .salary")
        position_name = title.replace(salary, "")
        let create = await getElementText(page, ".time")
        create_time = create.replace("更新于：", "")
        let vline = await page.$eval("#main > div.job-banner > p", e => e.innerHTML)
        let vlineArr = vline.split(`<em class="vline"></em>`)
        let work_year = vlineArr[1]
        if (work_year.indexOf("年") == -1) {
            work_year = "不限"
        }
        
        let educational = vlineArr[vlineArr.length - 1]
        salary = parseSalary(salary)
        let company_name = await getElementText(page, ".business-info h4")
        let body = await page.$$eval(".job-sec .text", e => e.map(l => l.textContent).join("\n"))
        let address = await getElementText(page, ".location-address")
        let gray = await page.$eval(".job-company .gray", e => e.innerHTML)
        let grayArr =  gray.split(`<em class="vline"></em>`)
        let company_url = await page.$eval(".link-all",a=>a.href)
        let company_scale = grayArr[2] || ""
        let company_stage =  grayArr[1] || ""
        let company_area = grayArr[0] || ""
        let map = await page.evaluate(()=>{
            let long_lat = document.getElementById('map-container').getAttribute("data-long-lat");
            return long_lat
        });
        map = map.split(",")
        let company_info = {
            company_id:getIdByUrl(company_url),
            company_name:company_name.replace(/\s+/g,""),
            company_scale:company_scale.replace(/\s+/g,""),//公司规模
            company_stage:company_stage.replace(/\s+/g,""), //发展阶段
            company_area: company_area.replace(/\s+/g,""),//公司领域
            company_site:company_url,//公司网站
            position_lng: map[0],
            position_lat: map[1],
        }
        return {
            address,
            salary,
            create_time,
            body,
            company_name,
            postion_id,
            position_name,
            educational,
            work_year,
            company_info
        }

    } catch (error) {
        console.log(error)
        return false
    }
}
(async () => {
    try {
        const browser = await spider.launch();
        const page = await browser.newPage();
        const reset = require("../lib/resetChorme");
        await reset(page);
        await page.setUserAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36");
        await page.setViewport({ width: 1280, height: 926 });
        const resp = await page.goto("https://m.zhipin.com/c101020100-p100103/?ka=position-100103")
        //console.log("响应code:" + resp.status() + "url"+ resp.url())
        const items = await scrapeInfiniteScrollItems(page, extractItems, 10);
        let results = []
        for (let index = 0; index < items.length; index++) {
            let url = items[index];
            let res = await gotoDetail(page, url)
            if (res == false) {
                continue;
            }
            results.push(res)
            await page.waitFor(2000);
        }
        console.log("total:", results.length)
        await browser.close();
    } catch (e) {
        console.log(e)
        process.exit(1)
    }
})();