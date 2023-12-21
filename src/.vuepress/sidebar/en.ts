import {sidebar} from "vuepress-theme-hope";

export const enSidebar = sidebar({
    "/notes/": [{
        text: "Notes",
        prefix: "",
        children: "structure",
    }],
    "/research/": [{
        text: "Research",
        prefix: "",
        children: "structure",
    }],
    "/body/": [{
        text: "Body",
        prefix: "",
        children: "structure",
    }],
    "/portfolio/": [{
        text: "Portfolio",
        prefix: "",
        children: "structure",
    }]
});
