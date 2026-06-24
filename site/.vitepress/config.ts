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
          "680 exercises, 52 programs, 6 training systems. Evidence-tiered.",
      },
    ],
  ],

  themeConfig: {
    logo: undefined,
    siteTitle: "Barlore",

    nav: [
      { text: "Home", link: "/" },
      { text: "Exercises", link: "/exercises/" },
      { text: "Programs", link: "/programs/" },
      { text: "Training Science", link: "/core/" },
      { text: "Nutrition & Recovery", link: "/crosscutting/" },
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
