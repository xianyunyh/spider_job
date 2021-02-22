import puppeteer from "puppeteer";

class Browser {
  private browser: puppeteer.Browser | undefined;
  constructor(args: puppeteer.LaunchOptions) {
  }
  async newPage() {
    return await this.browser?.newPage();
  }
  async close() {
    await this.browser?.close()
  }
  async create(options: puppeteer.LaunchOptions):Promise<puppeteer.Browser> {
     options = {
      executablePath: "",
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox'],
      defaultViewport: {
        width: 1440,
        height: 720,
      },
      timeout: 60000,
      ...options,
    }
    const browser = await puppeteer.launch(options)
    this.browser = browser;
    return browser;
  }
}
export default Browser
