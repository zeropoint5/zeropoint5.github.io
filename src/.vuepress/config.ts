import { defineUserConfig } from "vuepress";
import theme from "./theme.js";

export default defineUserConfig({
  base: "/",

  locales: {
    "/": {
      lang: "en-US",
      title: "1/2 Station",
      description: "Hi there, I'm Bing Wang"
    },
    "/zh/": {
      lang: "zh-CN",
      title: "二分之一站台",
      description: "你好呀，我是王兵",
    },
  },

  theme,

  // Enable it with pwa
  // shouldPrefetch: false,
});
