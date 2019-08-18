## 爬虫项目

这是一个基于puppeteer的爬虫项目。爬虫的目标网站拉钩和boss直聘网。
由于puppeteer依赖chromium。但是在国内可能需要 `FQ` 所以建议单独下载chromium.改变配置文件中的chromium的执行路径。
linux用户推荐使用Centos 7
- [puppeteer文档](https://zhaoqize.github.io/puppeteer-api-zh_CN/#/class-Page)
- [chromium下载地址](https://npm.taobao.org/mirrors/chromium-browser-snapshots/)

### 安装
强烈建议先手动下载chromium。 本项目开始时候使用的版本号为`599821`

- linux用户
```bash
bash install.sh
```
- windows 用户

```bash
npm install  --ignore-scripts #跳过下载chromium
```

### 配置

windows用户 安装完node的依赖之后和下载了chromium。然后打开`lib/spider.js`
 将`executablePath` 改为下载chrome的执行路径chromium
然后执行 `node src/zhipin.js` 即可

如果不需要在前台看到浏览器，那么将`headless`的值改成 `true`
```js
splider.launch = async (option = {}) => {
  return await puppeteer.launch({
    executablePath: path.resolve(__dirname,'../chrome-win/chrome.exe'),
    headless: false,
    defaultViewport:{
      width:1440,
      height:720
    },
    timeout:6000,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
      ...option
  });
};
```



