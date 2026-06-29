import { defineConfig } from "vitepress";

export default defineConfig({
  title: "Barlore",
  description:
    "Strength & physique training encyclopedia — exercises, programs, and training science.",
  base: "/barlore/",
  srcDir: "src",
  cleanUrls: true,
  ignoreDeadLinks: true,

  sitemap: {
    hostname: "https://hollis-png.github.io/barlore",
  },

  head: [
    ["meta", { name: "google-site-verification", content: "mAwnB2ua-AOWNUhpis2FLDDwfrtGvZD0wpu3qn5aCuw" }],
    ["meta", { name: "theme-color", content: "#1a1a2e" }],
    ["meta", { property: "og:type", content: "website" }],
    [
      "meta",
      {
        property: "og:title",
        content: "Barlore — Training Encyclopedia",
      },
    ],
    [
      "meta",
      {
        property: "og:description",
        content:
          "688 exercises, 53 programs, 6 training systems. Evidence-tiered.",
      },
    ],
  ],

  locales: {
    root: {
      label: "English",
      lang: "en",
    },
    "zh-TW": {
      label: "繁體中文",
      lang: "zh-TW",
      themeConfig: {
        nav: [
          { text: "首頁", link: "/zh-TW/" },
          { text: "學習", link: "/zh-TW/learn" },
          { text: "動作庫", link: "/exercises/" },
          { text: "計畫", link: "/programs/" },
          { text: "訓練科學", link: "/core/" },
          { text: "營養與恢復", link: "/crosscutting/" },
          { text: "術語表", link: "/glossary" },
          {
            text: "AI 工具",
            items: [
              { text: "AI 使用指南", link: "/ai" },
              { text: "完整索引 (llms.txt)", link: "/llms-full" },
            ],
          },
        ],
        footer: {
          message: "以證據分級的訓練知識庫。",
          copyright: "Barlore Project",
        },
        darkModeSwitchLabel: "外觀",
        sidebarMenuLabel: "選單",
        returnToTopLabel: "回到頂部",
        docFooter: {
          prev: "上一頁",
          next: "下一頁",
        },
        outline: {
          label: "本頁目錄",
        },
        lastUpdated: {
          text: "最後更新",
        },
        search: {
          provider: "local",
          options: {
            translations: {
              button: { buttonText: "搜尋", buttonAriaLabel: "搜尋" },
              modal: {
                noResultsText: "找不到結果",
                resetButtonTitle: "清除搜尋",
                footer: { selectText: "選擇", navigateText: "切換", closeText: "關閉" },
              },
            },
          },
        },
      },
    },
  },

  themeConfig: {
    logo: undefined,
    siteTitle: "Barlore",

    nav: [
      { text: "Home", link: "/" },
      { text: "Learn", link: "/learn" },
      { text: "Exercises", link: "/exercises/" },
      { text: "Programs", link: "/programs/" },
      { text: "Training Science", link: "/core/" },
      { text: "Nutrition & Recovery", link: "/crosscutting/" },
      { text: "Glossary", link: "/glossary" },
      {
        text: "For AI",
        items: [
          { text: "AI Usage Guide", link: "/ai" },
          { text: "Full Index (llms.txt)", link: "/llms-full" },
        ],
      },
    ],

    sidebar: {
      "/core/": [
        {
          text: "Training Science",
          items: [
            { text: "Progressive Overload", link: "/core/progressive_overload" },
            { text: "Periodization", link: "/core/periodization" },
            { text: "SRA Curve", link: "/core/sra_curve" },
            { text: "Volume Landmarks", link: "/core/volume_landmarks" },
            { text: "RPE & RIR", link: "/core/rpe_rir" },
            { text: "Rep Continuum", link: "/core/rep_continuum" },
            { text: "Specificity (SAID)", link: "/core/specificity" },
            { text: "Hypertrophy Mechanisms", link: "/core/hypertrophy_mechanisms" },
            { text: "Training to Failure", link: "/core/training_to_failure" },
            { text: "Testing Protocols", link: "/core/testing_protocols" },
            { text: "Deload", link: "/core/deload" },
          ],
        },
      ],
      "/crosscutting/": [
        {
          text: "Nutrition",
          items: [
            { text: "Protein", link: "/crosscutting/protein_requirements" },
            { text: "Carbohydrates", link: "/crosscutting/carbohydrate_requirements" },
            { text: "Fat", link: "/crosscutting/fat_requirements" },
            { text: "Energy Balance", link: "/crosscutting/energy_balance" },
            { text: "Nutrient Timing", link: "/crosscutting/nutrient_timing" },
            { text: "Hydration", link: "/crosscutting/hydration" },
            { text: "Supplementation", link: "/crosscutting/supplementation" },
            { text: "Body Recomposition", link: "/crosscutting/body_recomposition" },
          ],
        },
        {
          text: "Recovery",
          items: [
            { text: "Sleep", link: "/crosscutting/sleep" },
            { text: "Warm-Up", link: "/crosscutting/warm_up" },
            { text: "Active Recovery", link: "/crosscutting/active_recovery" },
            { text: "Deload Protocol", link: "/crosscutting/deload_protocol" },
          ],
        },
        {
          text: "Injury Prevention",
          items: [
            { text: "Connective Tissue", link: "/crosscutting/connective_tissue" },
            { text: "Load Management", link: "/crosscutting/load_management" },
            { text: "Mobility", link: "/crosscutting/mobility_requirements" },
            { text: "Overtraining Signs", link: "/crosscutting/overtraining_signs" },
          ],
        },
        {
          text: "Cardio",
          items: [
            { text: "Aerobic Base", link: "/crosscutting/aerobic_base" },
            { text: "Concurrent Training", link: "/crosscutting/concurrent_training" },
            { text: "HIIT Protocol", link: "/crosscutting/hiit_protocol" },
          ],
        },
        {
          text: "Special Populations",
          items: [
            { text: "Beginner Lifters", link: "/crosscutting/beginner_lifters" },
            { text: "Female Athletes", link: "/crosscutting/female_athletes" },
            { text: "Masters (35+)", link: "/crosscutting/masters_athletes" },
          ],
        },
      ],
    },

    search: {
      provider: "local",
    },

    socialLinks: [
      { icon: "github", link: "https://github.com/hollis-png/barlore" },
    ],

    footer: {
      message: "Evidence-tiered training knowledge.",
      copyright: "Barlore Project",
    },
  },

  // Allow unknown frontmatter fields from exercise/program files
  markdown: {
    frontmatter: {
      grayMatterOptions: {
        excerpt: false,
      },
    },
  },
});
