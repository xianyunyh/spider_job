module.exports = {
    // 基本路径
    baseUrl: '/job/',
    outputDir: 'dist',

    devServer: {
     open: process.platform === 'darwin',
     host: '0.0.0.0',
     port: 8080,
     https: false,
     hotOnly: false,
     proxy: null, // 设置代理
    },
    // 第三方插件配置
    pluginOptions: {
     // ...
    }
   }