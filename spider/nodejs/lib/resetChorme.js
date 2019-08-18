const randomUserAgent = require('../config/user-agents');
module.exports = async function(page) {
  // Pass the User-Agent Test.
  const userAgent = randomUserAgent();
  await page.setUserAgent(userAgent);

  // Pass the Webdriver Test.
  await page.evaluateOnNewDocument(() => {
    const newProto = navigator.__proto__;
    delete newProto.webdriver;
    navigator.__proto__ = newProto;
  });

  // Pass the Chrome Test.
  await page.evaluateOnNewDocument(() => {
    // We can mock this in as much depth as we need for the test.
    window.chrome = {
      runtime: {}
    };
  });

  // Pass the Permissions Test.
  await page.evaluateOnNewDocument(() => {
    const originalQuery = window.navigator.permissions.query;
    window.navigator.permissions.__proto__.query = parameters =>
        parameters.name === 'notifications'
            ? Promise.resolve({state: Notification.permission})
            : originalQuery(parameters);

    // Inspired by: https://github.com/ikarienator/phantomjs_hide_and_seek/blob/master/5.spoofFunctionBind.js
    const oldCall = Function.prototype.call;
    function call() {
      return oldCall.apply(this, arguments);
    }
    Function.prototype.call = call;

    const nativeToStringFunctionString = Error.toString().replace(/Error/g, "toString");
    const oldToString = Function.prototype.toString;

    function functionToString() {
      if (this === window.navigator.permissions.query) {
        return "function query() { [native code] }";
      }
      if (this === functionToString) {
        return nativeToStringFunctionString;
      }
      return oldCall.call(oldToString, this);
    }
    Function.prototype.toString = functionToString;
  });

  // Pass the Plugins Length Test.
  await page.evaluateOnNewDocument(() => {
    // Overwrite the `plugins` property to use a custom getter.
    Object.defineProperty(navigator, 'plugins', {
      // This just needs to have `length > 0` for the current test,
      // but we could mock the plugins too if necessary.
      get: () => [1, 2, 3, 4, 5]
    });
  });

  // Pass the Languages Test.
  await page.evaluateOnNewDocument(() => {
    // Overwrite the `plugins` property to use a custom getter.
    Object.defineProperty(navigator, 'languages', {
      get: () => ['en-US', 'en']
    });
  });

  // Pass the iframe Test
  await page.evaluateOnNewDocument(() => {
    Object.defineProperty(HTMLIFrameElement.prototype, 'contentWindow', {
      get: function() {
        return window;
      }
    });
  });

  // Pass toString test, though it breaks console.debug() from working
  await page.evaluateOnNewDocument(() => {
    window.console.debug = () => {
      return null;
    };
  });
};
