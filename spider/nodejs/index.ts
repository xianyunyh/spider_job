import Browser from './src/utils/spider'
(async () => {
    const browser = new Browser({});
    await browser.create({ executablePath: "", headless: true });
    const page = await browser.newPage();
    if (!page) {
        await browser.close();
        return
    }
    await page.goto('https://baidu.com');
    await page.screenshot({path: 'example.png',fullPage:true});
    await browser.close();
})();