import { pino } from "pino";

export default pino({
  base: {},
  timestamp: () => `,"time":"${new Date().toLocaleString()}"`,
  messageKey: "msg",
  formatters: {
    level(label) {
      return { level: label }
    }
  }
});