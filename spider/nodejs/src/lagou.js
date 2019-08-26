const spider = require('../lib/spider');
const Url = require('url-parse');
const trim = require('trim');
const dayjs = require("dayjs")
async function getList(page, url) {
    try {
        const resp = await page.goto(url);
        await page.waitFor(1000)
        $ = cheerio.load(resp.text)
        return $(".item a").each(function (e) {
            return e.href
        })
    } catch (e) {
        return false;
    }
}
function extractItems() {
    const extractedElements = document.querySelectorAll('.s_position_list  .item_con_list li .position a');
    const items = [];
    for (let element of extractedElements) {
        items.push(element.href);
    }
    return items;
}

async function getListItems(
    page,
    extractItems,
    itemTargetCount,
    scrollDelay = 1000,
) {

    try {
        let items = await page.evaluate(extractItems);
        while (items.length < itemTargetCount) {
            await page.click(".pager_container .pager_next", { delay: 500 })
            temp = await page.evaluate(extractItems);
            items = [...items, ...temp]
            await page.waitFor(scrollDelay);
        }
        return items;
    } catch (e) {
        console.log(e)
        return false;
    }

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

function parseTime(t) {
    t = trim(t)
    if (t.length == 0) {
        return ""
    }
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
    const parseMoney = (m) => {
        step = 1
        m = m.toLocaleUpperCase()
        if (m.indexOf("W") > 0) {
            m = m.replace("W","")
            step = 10000
        } else if (m.indexOf("K") > 0) {
            m = m.replace("K","")
            step = 1000
        }
        return parseFloat(m) * step
    }
    
    temp.min = parseMoney(min)
    temp.max = parseMoney(max)
    temp.avg = parseInt((temp.min + temp.max) / 2)
    return temp
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

function parseWorkYear(w) {
    const wks = ["毕业生","1-3年","3-5年","5-10年","10年以上","经验不限"]
    for (let element of wks) {
        if (w.indexOf(element) >=0 ) {
            return element
        }
      }
      return "经验不限"
}

function getIdByUrl(url) {
    let uParse = new Url(url)
    let path = uParse.pathname
    pathArr = path.split("/")
    return pathArr[pathArr.length - 1].replace(".html", "")
}
async function gotoDetail(page, url) {
    try {
        await page.goto(url)
        await page.waitForSelector("body")
        
        postion_id = getIdByUrl(url)
        let title = await getElementText(page, "h2.name")
        let salary = await getElementText(page, ".salary")
        let create = await getElementText(page, ".publish_time")
        let work_year = await getElementText(page, ".job_request span:nth-child(3)")
        let educational = await getElementText(page, ".job_request span:nth-child(4)")
        let company_name = await getElementText(page, ".job_company_content .fl-cn") 
        let body = await getElementText(page, ".job-detail")
        let address = await getElementText(page, ".work_addr")
        let company_url = await page.$eval("#job_company > dt > a",a=>a.href)
        let company_scale = await getElementText(page,"#job_company > dd > ul > li:nth-last-child(2)  h4")
        let company_stage =  await getElementText(page,"#job_company > dd > ul > li:nth-child(2)  h4")
        let company_area = await getElementText(page,"#job_company > dd > ul > li:nth-child(1)  h4")
        let company_site = await page.$eval("#job_company > dd > ul > li:nth-last-child(1)  a",a=>a.href)
        let company_info = {
            company_id:getIdByUrl(company_url),
            company_name:company_name.replace(/\s+/g,""),
            company_scale:company_scale,//公司规模
            company_stage:company_stage, //发展阶段
            company_area: company_area,//公司领域
            company_site:company_site,//公司网站
            position_lng: await page.$eval("input[name=positionLng]",input=>input.value),
            position_lat: await page.$eval("input[name=positionLat]",input=>input.value),
        }
        return {
            postion_id,
            body,
            address:address.replace("查看地图","").replace(/\s+/g,""),
            salary:parseSalary(salary),
            create_time:parseTime(create.replace("发布于拉勾网", "")),
            company_name:company_name.replace(/\s+/g,""),
            position_name:title.replace(salary, ""),
            educational:parseEdu(educational),
            work_year:parseWorkYear(work_year),
            from_site:"lagou",
            company_info,
        }

    } catch (error) {
        console.log(error)
        return false;
    }
}
(async () => {
    try {
        const browser = await spider.launch();
        const page = await browser.newPage();
        const resetChorme  = require("../lib/resetChorme")
        await resetChorme(page)
        await page.setUserAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36");
        await page.setViewport({ width: 1280, height: 926 });
        
        await page.goto("https://www.lagou.com/jobs/list_PHP?px=new&city=%E4%B8%8A%E6%B5%B7#order")
        let items = await getListItems(page, extractItems, 40, 5000)
        for (let index = 0; index < items.length; index++) {
            let url = items[index];
            let res = await gotoDetail(page, url)
            if (res == false) {
                continue;
            }
            console.log(res)
            await page.waitFor(2000);
        }
       // console.log(res)

        await browser.close();
    } catch (e) {
        console.log(e)
        //process.exit(1)
    }
})();