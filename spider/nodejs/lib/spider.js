const puppeteer = require('puppeteer');
const path = require('path');
const splider = {};
splider.launch = async (option = {}) => {
  return await puppeteer.launch({
    executablePath: "",
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
module.exports = splider;
