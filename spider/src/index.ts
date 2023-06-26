import puppeteer from 'puppeteer-extra'
import StealthPlugin from 'puppeteer-extra-plugin-stealth'
import zhipin from './spider/zhipin'
import { PuppeteerLaunchOptions } from 'puppeteer'
import logger from './utils/log'
logger.info("111")


const options: PuppeteerLaunchOptions  = {
  // 启动无头浏览器
  headless: 'new',
  // 浏览器路径
  executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
}
puppeteer.use(StealthPlugin()).launch(options)
  .then(async browser => {
    const page = await browser.newPage()
    try {
      await zhipin.run(page, "https://www.zhipin.com/c101020100-p100103/");
      await browser.close()
    }
    catch(e){
      logger.error(`load page error ${page.url()} error:${e}`)
    }finally{
      await browser.close()
    }
    
  }).catch(e => console.log(e))