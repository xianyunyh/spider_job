import { Page, EvaluateFunc } from "puppeteer";
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
}