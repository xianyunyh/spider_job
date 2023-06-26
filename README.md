# 爬虫项目

## 免责声明

<font color="red" size="14">本软件仅用于学术研究，但因在中国大陆频频出现爬虫开发者涉诉与违规相关的[新闻](https://github.com/HiddenStrawberry/Crawler_Illegal_Cases_In_China)。<br></font>

<h3>使用者需遵守其所在地的相关法律法规。因违法违规使用造成的一切后果，使用者自行承担</h3>
这个项目是主要自己研究招聘网站上的职位以及对应的需求准备的一个爬虫项目。
爬虫项目基于`nodejs` `puppeteer`框架进行爬虫，使用`mysql` 存储爬取数据。
服务端界面使用`nodejs`  `koajs` 实现了一个`web` `ui`展示

- 项目目录结构图

```

├─web 后端服务
├─spider python爬虫
│  ├─src/spider        爬虫实现
│  │  ├─zhipin.ts      直聘爬虫
├─word.json 生成的英文技术词json
├─word.py 生成英文分词
├─stop.txt 停用词列表
```

## 后端服务

后端服务是使用`koajs`编写的一个接口和展示数据的服务。

打开`web/server/config/index.ts` 修改自己的数据库的信息

```shell
cd web
npm install --registry https://registry.npmmirror.com/
#启动服务
npm run dev
```

## 运行爬虫

- 请安装`Nodejs` 

- 需要本地安装 `chrome`、或者`edge`浏览器

  打开`spider/src/index.ts`

  修改 `executablePath` 成 本地的浏览器路径

  ```js
  const options: PuppeteerLaunchOptions  = {
    // 启动无头浏览器
    headless: 'new',
    // 浏览器路径
    executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
  }
  ```

  ```shell
  cd spider
  npm install --registry https://registry.npmmirror.com/  --ignore-scripts #跳过下载chromium
  #运行服务
  npm run dev
  #编译
  npm run build
  ```

  