import { Page, EvaluateFn } from "puppeteer";
export class Spider {
    protected page: Page
    constructor(page: Page) {
        this.page = page
    }
    async getElementText(selector: string): Promise<string> {
        try {
            await this.page.waitForSelector(selector);
            return await this.page.$eval(selector, ele => ele.textContent || '');
        } catch (e) {
            return "";
        }
    }
    extractItemLinks(selector: string): Array<string> {
        const extractedElements = document.querySelectorAll(selector);
        let items: Array<string> = [];
        extractedElements.forEach(element => {
            items.push(element.getAttribute("href") || '')
        })
        return items;
    }
    async scrapeInfiniteScrollItems(extractItems: EvaluateFn, itemTargetCount: number, scrollDelay: number = 1000): Promise<Array<string>> {
        let items: Array<string> = [];
        const page = this.page
        try {
            let previousHeight;
            while (items.length < itemTargetCount) {
                items = await this.page.evaluate(extractItems) as Array<string>;
                previousHeight = await page.evaluate('document.body.scrollHeight');
                await page.evaluate('window.scrollTo(0, document.body.scrollHeight)');
                await page.waitForFunction(`document.body.scrollHeight > ${previousHeight}`);
                await page.waitFor(scrollDelay);
            }
        } catch (e) {
            console.log(e)
            return [];
        }
        return items;
    }
}