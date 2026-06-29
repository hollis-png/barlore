import DefaultTheme from "vitepress/theme";
import type { Theme } from "vitepress";
import EvidenceBadge from "./EvidenceBadge.vue";
import { h } from "vue";

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      "doc-before": () => h(EvidenceBadge),
    });
  },
} satisfies Theme;
