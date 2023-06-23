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
    await zhipin.run(page, "https://www.zhipin.com/c101020100-p100103/");
    await browser.close()
  }).catch(e => console.log(e))