import Browser from './src/utils/spider'
import ZhiPin from './src/zhipin'
import lagou from './src/lagou'
(async () => {
    const browser = new Browser({});
    await browser.create({ executablePath: "",headless: false });
    try {
        const page = await browser.newPage();
        if (!page) {
            await browser.close();
            console.log("page create error")
            return
        }
        const sp = new lagou(page)
        await sp.run("");
        await browser.close();
        process.exit(0)
    } catch (error) {
        console.log((error as Error).message)
        await browser.close();
        process.exit(-1)
    }
    
})();