/* 33077.com — site configuration. Edit values here; no other file needs changing. */
window.SITE = {
  name: "33077",
  tagline: "The Chinese Number Code Hub",
  interestUrl: "https://web.works/contact",

  /* Owner inbox for ALL forms. Stored encoded + reversed so it never appears in page text or source.
     After the first submission FormSubmit sends a one-time activation email; once activated you may
     replace `inbox` with the random FormSubmit alias it gives you (set inboxIsAlias: true). */
  inbox: ["=02b",  "j5Cb",  "pFWb",  "nBUM",  "hN3a",  "y92d",  "iV2d"],
  inboxIsAlias: false,

  /* Google AdSense — paste your publisher id (e.g. "ca-pub-1234567890123456") to switch ads on.
     Leave empty to show house ads (sponsor slots) instead. Also update /ads.txt. */
  adsenseClient: "",
  adSlots: { top: "", content: "", sidebar: "", sticky: "" },

  /* Donations — paste any payment link to show its button. Empty = hidden; pledge form always works. */
  donate: {
    paypal: "",      /* e.g. https://www.paypal.com/donate/?hosted_button_id=XXXX */
    kofi: "",        /* e.g. https://ko-fi.com/yourname */
    buymeacoffee: "",/* e.g. https://buymeacoffee.com/yourname */
    stripe: ""       /* e.g. https://buy.stripe.com/XXXX */
  },
  fundingGoal: { label: "2027 Season Fund (Qixi campaign, contests, hiring)", goal: 3307, raised: 0, supporters: 0 },

  youtubeChannel: "", /* e.g. https://www.youtube.com/@33077 — shows a Subscribe button when set */
  videos: [
    { id: "pT52hREAf18", title: "Chinese Lucky Numbers", channel: "Numberphile" },
    { id: "gXoC6oubwDM", title: "88, 520, 5201314 in Chinese — Meanings", channel: "Everyday Chinese" },
    { id: "wf13M4MoHS4", title: "Chinese Lucky and Unlucky Numbers Explained", channel: "Learn Chinese Now" },
    { id: "sr673iAqLZY", title: "Meanings behind Chinese numbers", channel: "Chinese with Christine" },
    { id: "8iKXzijkSMg", title: "What Is Qixi? The Ancient Chinese Valentine's Day", channel: "WION" },
    { id: "0eOWWuXpSZw", title: "The Legend of the Cowherd and the Weaver Girl", channel: "Prince in Apron" },
    { id: "p1aXXPVPqIA", title: "Why is 8 considered lucky in Chinese culture?", channel: "Let's Chinese" }
  ],

  contest: {
    name: "The 33077 Love Code Challenge",
    closes: "2027-08-08T23:59:00+08:00", /* Qixi 2027 */
    prizes: [
      { place: "Grand Prize", prize: "US$333 + featured on the homepage for a year" },
      { place: "2 Runners-up", prize: "US$77 each + winner badge" },
      { place: "10 Honourable mentions", prize: "Featured on the Love Code Wall" }
    ]
  }
};
