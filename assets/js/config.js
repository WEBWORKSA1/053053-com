/* =========================================================
   053053.com — site configuration (the only file you edit)
   ========================================================= */
window.SITE = {
  name: "053053 · Number Intelligence & Scam Shield",
  domain: "053053.com",
  partnerContact: "https://web.works/contact",

  /* Google AdSense. The publisher id is live, so Auto Ads load on every page.
     Paste ad-unit slot ids below to turn the reserved slots into manual units; an empty slot shows a house ad. */
  ADSENSE_CLIENT: "ca-pub-6620975821265271",
  AD_SLOTS: { inContent: "", sidebar: "", result: "", footer: "" },

  /* YouTube: channel URL and video ids. An empty list shows curated cards that open a YouTube search. */
  YOUTUBE_CHANNEL: "",
  VIDEOS: [
    // { id: "VIDEO_ID", title: "Wangiri one-ring scam explained", topic: "Scams" },
  ],

  /* Donations: paste payment links when ready. Empty means the pledge form is used. */
  DONATE: { paypal: "", kofi: "", bmac: "", stripe: "", patreon: "" },
  DONATION_GOAL: { label: "Season 1 · moderation, translators & Scam Spotter prizes", raised: 0, goal: 5300 },

  /* Analytics: GA4 measurement id, e.g. "G-XXXXXXX" */
  GA4: ""
};

/* Contact routing: obfuscated and assembled only at submit time. Never replace with plain text. */
window.__r = [71,80,81,71,90,65,70,23,4,82,47,3,8,81,92,95,30,86,92,64];
window.__k = "053053-decode";
