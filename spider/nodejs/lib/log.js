const log4js = require('log4js');
const enviroment = process.env.DEBUG || 'product';
const path = require('path');
const appenders = [enviroment];
log4js.configure({
    appenders: {
        product: {
            type: 'file',
            filename:    path.resolve(__dirname,'../spider.log'),
            maxLogSize: 2048000,
            numBackups: 10,
        },
        develop: {
            type: 'console',
        }
    },
    categories: {
        default: {
            appenders: appenders,
            level: 'info'
        }
    }
});
const logger = log4js.getLogger(enviroment);
logger.level = 'debug';
module.exports = logger;
