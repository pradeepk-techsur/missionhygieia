# Mission Hygieia — Website

A multi-page static site for Mission Hygieia. The visual and verbal system is documented in `STYLE_GUIDE.md` — read that first before making any change.

## Files

```
mission-hygieia-site/
├── STYLE_GUIDE.md    ← The brand system. Source of truth.
├── README.md         ← This file.
├── styles.css        ← Implements the style guide.
├── index.html        ← Homepage
├── our-kits.html
├── our-team.html
├── shelters.html
├── blog.html
├── contact.html
└── donate.html
```

The site is **fully self-contained** — it works the moment you open `index.html`. There are zero required image files.

## Brand at a glance

- **Color:** Mission blue `#014D75` and white. Rust `#B85528` reserved for the donate button only.
- **Type:** Lora (headlines), Inter (everything else). Both from Google Fonts.
- **Cost per kit:** $3.50. The donation tier ladder runs $3.50 / $7 / $35 / $175 / $350.

## Logo

The site looks for a file named `logo.png` in this folder. **If it exists, every page automatically uses it** in the nav top-left and the footer. If it doesn't exist, every page falls back to a clean typographic mark (a small Mission-blue circle paired with "Mission Hygieia" set in Lora).

To use your real logo: save the existing missionhygieia.org logo as `logo.png` in this folder. That's it. Nothing else to edit.

The supporter logos work the same way: drop in `bfs.png` and `techsur.png` to replace the placeholder marks on the homepage.

## Running the site

Three options, easiest first.

### 1. Just open it
Double-click `index.html`. Browser opens it via `file://`. Every link works.

### 2. Local server (one command)
```bash
python -m http.server 8000     # macOS, Linux, or Windows with Python installed
```
Then visit `http://localhost:8000`.

### 3. Deploy to a real URL
Drag the folder onto **[netlify.com/drop](https://app.netlify.com/drop)**. Free, public URL in 30 seconds, no account required.

## Editing

**For color, type, or spacing changes** — start in `STYLE_GUIDE.md`. Decide the rule, then change `styles.css` to match. Most palette and spacing changes are one-line edits at the top of the stylesheet.

**For copy changes** — edit the relevant `.html` file. Each page is self-contained.

**For voice and tone** — read section 7 of the style guide before writing. The "read aloud test" catches most missteps.

## What's still placeholder

A few things in the site are illustrative and need to be replaced before going live:

- **Logo file** — drop in your real `logo.png` to replace the typographic placeholder.
- **Supporter logos** — drop in `bfs.png` and `techsur.png` to replace the abstract placeholder marks.
- **All numerical figures** — kit counts and percentage breakdowns are placeholders. Replace with verified numbers before publishing.
- **All blog post titles and dates** on `blog.html` — these are illustrative.
- **Founder bio quotes and role descriptors** on `our-team.html` — have each founder write a sentence or two in their own voice.
- **The donate form doesn't actually charge cards.** It's a UI shell. To make it real, replace the form with a Stripe Checkout link, Donorbox embed, or Givebutter widget.
- **The contact form doesn't actually send mail.** Use Netlify Forms (free, just add `data-netlify="true"` to the `<form>` tag if you deploy on Netlify), Formspree, or Web3Forms.

## Going live

1. Deploy to Netlify, Vercel, or Cloudflare Pages first (test on their `*.netlify.app` URL).
2. Wire up real donation processing and the contact form.
3. Add the logo file and supporter logo files.
4. Take and add at least one real photograph (per the style guide, illustrations should not be used).
5. Update placeholder numbers and quotes.
6. Move the `missionhygieia.org` domain to the new host.
7. Cancel the Zyro subscription once DNS has propagated.
