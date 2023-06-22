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

windows用户 安装完node的依赖之后和下载了chromium。然后打 'index.ts'
 将`executablePath` 改为下载chrome的执行路径chromium
然后执行 `npx ts-node src/index.ts` 即可
或者执行`npm run build` 编译ts到js 然后再运行 `node dist/index.js`

如果不需要在前台看到浏览器，那么将`headless`的值改成 `true`
```js
 puppeteer.launch({
    // 启动无头浏览器
    headless: false,
    // 浏览器路径
    executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
  })
```



