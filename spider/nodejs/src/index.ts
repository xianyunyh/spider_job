import puppeteer from 'puppeteer-extra'
import StealthPlugin from 'puppeteer-extra-plugin-stealth'
import zhipin from './spider/zhipin'
puppeteer
  .use(StealthPlugin())
  .launch({
    // 启动无头浏览器
    headless: false,
    // 浏览器路径
    executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
  })
  .then(async browser => {
    const page = await browser.newPage()
    const conf = {
      start_url: "https://www.zhipin.com/web/geek/job",
      city_code: "101020100",
      position: "100103",
    }
    await zhipin.run(page, conf);
    await browser.close()
  }).catch(e => console.log(e))