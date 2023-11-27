import {sidebar} from "vuepress-theme-hope";

export const zhSidebar = sidebar({
    "/zh/notes/": [{
        text: "笔记",
        prefix: "",
        children: "structure",
    }],
    "/zh/academic/": [{
        text: "学术",
        prefix: "",
        children: "structure",
    }],
    "/zh/body/": [{
        text: "身体",
        prefix: "",
        children: "structure",
    }],
    "/zh/portfolio/": [{
        text: "作品集",
        prefix: "",
        children: "structure",
    }]
});
