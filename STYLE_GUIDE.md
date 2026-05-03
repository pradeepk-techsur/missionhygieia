# Mission Hygieia — Style Guide

The source of truth for every visual and verbal decision on this site. If you're about to make a change and it's not covered here, ask whether the rule should be added here first, then make the change.

---

## 1. Brand foundation

**What this brand has to do:** Convince a stranger to give $3.50 (or more), recruit student volunteers, and read as a legitimate 501(c)(3) to shelter directors and corporate sponsors. All three at once.

**Emotional register:** Quiet dignity. Not high-energy youth, not sentimental charity, not corporate gloss. The work is delivering basic respect to people who've been overlooked — the brand should feel like that work, not louder than it.

**Visual metaphor:** Hand-packed. Every kit is assembled by volunteers around folding tables. The brand can have small handmade touches without tipping into "scrapbook." Restraint separates "considered" from "amateur."

**One-line test for any decision:** Does this make us look like a peer of Charity:Water and ProPublica, or a peer of a school club website? Aim for the first.

---

## 2. Color

The brand uses **two primary colors** (Mission Hygieia blue and white) plus neutrals, with **one warm accent** reserved exclusively for conversion actions.

### The palette

| Role                      | Name              | Hex       | When to use                                                                          |
| ------------------------- | ----------------- | --------- | ------------------------------------------------------------------------------------ |
| **Brand color**           | **Mission blue**  | `#014D75` | Logo lockup, headlines that need emphasis, link color, key icons. ~10% of any view.  |
| Brand color — soft        | Pale blue         | `#E5EEF4` | Tinted backgrounds for callout boxes, hover states, sidebar surfaces.                |
| Brand color — deep        | Deep blue         | `#013A5A` | Hover state for blue elements; only used as a darker variant.                        |
| Background canvas         | White             | `#FFFFFF` | Default page background.                                                             |
| Secondary surface         | Soft white        | `#F7F8FA` | When two surfaces sit next to each other and need tonal break.                       |
| Primary text & lines      | Near-black        | `#1A1A1A` | Body type, headlines, hairline borders.                                              |
| Secondary text            | Warm gray         | `#5A5A5C` | Captions, metadata, eyebrow labels, anything supporting.                             |
| Tertiary / dividers       | Soft gray         | `#D6D8DD` | Hairlines between repeating items, disabled states, input borders.                   |
| **Conversion accent**     | **Rust**          | `#B85528` | Donate button. The single most important action on the page. Nothing else.          |
| Conversion accent — hover | Deep rust         | `#9C4520` | Hover state for the donate button.                                                   |

### Usage rules

- **Mission blue is the brand expression.** Use it on the logo, headline accents, links, and one or two key icons per page. Never on body copy.
- **Rust is the rarest color in the system.** Reserved for the donate button. If you find yourself wanting rust on something that isn't a donation conversion action, choose a different solution. Rust on multiple elements per page kills its conversion power.
- **Pure black is forbidden for body copy under 16px.** Use `#1A1A1A` for headlines and `#5A5A5C` for body and captions to reduce eye strain.
- **No gradients.** Anywhere. Solid color only.
- **No drop shadows.** On text, on buttons, on cards. Use 1px hairline borders instead.

### Forbidden elsewhere on the brand

Yellows. Pinks and pastels. Stock-image gradients. Any third primary color. Multiple competing accents.

---

## 3. Typography

### The system: two typefaces

| Role                | Family   | Source                            |
| ------------------- | -------- | --------------------------------- |
| Headlines & display | **Lora** | Google Fonts                      |
| Everything else     | **Inter**| Google Fonts                      |

That's it. No script font, no monospace except for one specific use (data tables and code), no third typeface for any reason.

### Type scale

| Use                     | Family | Size (desktop) | Size (mobile) | Weight | Line height | Notes                                              |
| ----------------------- | ------ | -------------- | ------------- | ------ | ----------- | -------------------------------------------------- |
| Display (hero h1)       | Lora   | 64–72px        | 40–48px       | 400    | 1.05        | Used once per page. Never two on the same page.    |
| H1 (page header)        | Lora   | 48–56px        | 36–40px       | 400    | 1.1         |                                                    |
| H2 (section title)      | Lora   | 36–40px        | 28–32px       | 400    | 1.15        |                                                    |
| H3 (card title)         | Inter  | 20–22px        | 18–20px       | 600    | 1.25        | Sans for h3 — keeps sub-section weight balanced.   |
| H4 (small heading)      | Inter  | 16px           | 16px          | 600    | 1.3         |                                                    |
| Body large (lead)       | Inter  | 18–19px        | 17px          | 400    | 1.55        | Used directly under headlines, not throughout.     |
| Body                    | Inter  | 16–17px        | 16px          | 400    | 1.6         | Default.                                           |
| Body small / caption    | Inter  | 14px           | 13px          | 400    | 1.5         |                                                    |
| Eyebrow / label         | Inter  | 12–13px        | 12px          | 500    | 1.4         | All caps, letter-spacing 0.08em.                   |
| Big numbers / stats     | Lora   | 88–120px       | 64–80px       | 300    | 0.9         | Light weight only at this size.                    |
| Italic emphasis         | Lora   | inherits       | inherits      | 400    | inherits    | Italic serif replaces all "scribble" accents.      |

### Italics

Italics in Lora replace what was previously a script-font accent. Use italic serif when you want a quiet emphasis — a subordinate clause, an aside, the "feeling" word in a headline. Don't italicize whole sentences; italicize the one or two words that carry emotion.

Example: `Small kits. Big <em>dignity</em>.`

### Banned typography behavior

- **No all-caps body copy.** All-caps is reserved for eyebrow labels (12–13px) and never longer than 4–5 words.
- **No center-aligned long-form text.** Headlines occasionally; paragraphs never.
- **No bold inside body paragraphs for emphasis.** If a phrase needs emphasis, italicize it.
- **No font weights below 300 or above 700.**
- **Line length never exceeds 80 characters.** Body copy columns max out around 680px wide.

---

## 4. Layout & spacing

### The 8px baseline

All spacing values are multiples of 8: `8, 16, 24, 32, 48, 64, 96, 128`. Forces consistency without thinking.

### Section padding

| Context              | Desktop | Mobile |
| -------------------- | ------- | ------ |
| Major section        | 96px    | 64px   |
| Sub-section          | 64px    | 48px   |
| Card internal        | 32px    | 24px   |
| Between paragraphs   | 16px    | 16px   |

### Grid

Max content width: **1200px**. Reading-width content (long-form prose, FAQ): **680px**.

### Borders & dividers

- **Section transitions:** 1px hairline rule in `#1A1A1A`.
- **Card borders:** 1px in `#D6D8DD` (soft gray) for repeating list items. 1px in `#1A1A1A` only for emphasized cards.
- **Border radius:** 4px for inputs and small components, 8px for cards. Never 16px+. Never pill-shaped except on buttons.

### Whitespace

The single most important spacing rule: **err on the side of more.**

---

## 5. Buttons & links

### Buttons

| Style              | Background       | Text         | Border           | Use                                                  |
| ------------------ | ---------------- | ------------ | ---------------- | ---------------------------------------------------- |
| **Primary (rust)** | `#B85528` rust   | white        | none             | Donate. The single most important action per page.   |
| Secondary (blue)   | `#014D75` blue   | white        | none             | Important secondary actions.                         |
| Tertiary           | transparent      | `#1A1A1A`    | 1px `#1A1A1A`    | Default outlined button.                             |
| Quiet              | transparent      | `#014D75`    | none, underlined | Inline links, "read more" links.                     |

- **Padding:** 14px vertical, 28px horizontal.
- **Radius:** 4px. Never pill-shaped.
- **Font:** Inter, 15px, weight 500.
- **Hover:** 4–8% darken on background. No transform, no scale, no glow.

### Rule on button count

**One rust button per page.** That's the donate CTA. Multiple secondary (blue) buttons are fine. The rust's whole job is to be rare.

### Links

In body copy: `#014D75` Mission blue, underlined, 3px underline offset. Don't restyle links to look like body text — readers should be able to spot a link by scanning.

---

## 6. Imagery & illustration

**Real photography only.** Until real photography exists, use no imagery — typography and whitespace carry the page.

### Photography register

Documentary, warm, honest. Reference: Charity:Water annual reports, MSF brochures.

**What to photograph (in priority order):**

1. Real assembly days — kits laid out on folding tables, hands packing bags.
2. Shelter exteriors and supply rooms (with shelter director permission). **Never recipient faces.**
3. Founder portraits — single subjects against a plain wall, natural light.

**How to take it:** Phone camera. Natural light. No flash. No filters. Don't art-direct it. Shoot 30–50 frames; pick 2–3.

### When photos are missing

A typography-led hero with generous whitespace is the answer.

---

## 7. Voice & tone

### Three principles

1. **Specific over general.** "X kits delivered to six shelters across Loudoun and Fairfax counties" beats "making a real impact."
2. **Honest over heroic.** "We're three students. We work between classes." beats "Our dedicated team delivers excellence."
3. **Concrete over abstract.** "$3.50 covers eight items." beats "Your gift makes a difference."

### Tone rules

- **One exclamation point per page maximum.** Often zero.
- **No emoji in body copy.**
- **Banned words:** passionate, world-class, leverage, synergy, robust, innovative, transformative, game-changing, revolutionary.
- **Banned phrases:** make a difference, be the change, join the movement (unless literal), we couldn't do it without you.
- **No undenominated stats.** "X kits" with a real number — fine. "Thousands of lives changed" — banned.

### The read-aloud test

Read every paragraph out loud. If it sounds like a normal person talking to a friend, keep it. If it sounds like a press release, rewrite it.

### Headline guidance

Two parts when possible: a concrete claim, then a small qualifier or twist.
- Good: "Small kits. Big dignity."
- Good: "Three students. One stubborn idea."
- Bad: "Empowering communities through hygiene access."

Sentence case for body and most headers. Periods at the end of headlines are fine when the headline is a complete thought.

---

## 8. The numbers

| Metric                  | Value     | Note                                                     |
| ----------------------- | --------- | -------------------------------------------------------- |
| Cost per kit            | **$3.50** | All-in: supplies + tote + delivery, wholesale pricing.   |
| Kits delivered to date  | TBD       | Real count goes here once verified.                      |
| Shelter partners        | 6         | All in DMV / Northern Virginia + Haiti.                  |
| Founders                | 3         | Akhil Koranath, Sri Kasturi, Jhansi Chilakapati.         |

### Donation tier ladder

| Amount  | Kits  | Framing                                          |
| ------- | ----- | ------------------------------------------------ |
| $3.50   | 1     | A single kit for one person.                     |
| $7.00   | 2     | Two people start the day with a kit.             |
| $35     | 10    | Ten kits — a small drop-off run.                 |
| $175    | 50    | Roughly a month's supplies for a small shelter.  |
| $350    | 100   | A full corporate sponsorship.                    |

### Where every dollar goes (FY 2025)

- 87% supplies
- 10% logistics (totes, transit)
- 3% operations (domain, accounting, processing fees)

---

## 9. Components

### Stat blocks

Big number in Lora, light weight (300), 88–120px. Label below in Inter, 13px, all caps, letter-spacing 0.08em, color `#5A5A5C`. No card border — let the typography do it.

### Callout boxes

Pale blue background `#E5EEF4`, no border, 32px padding, max 600px wide.

### Quotes & testimonials

Lora italic, 22–28px, color `#1A1A1A`. Attribution underneath in Inter, 14px, weight 500, color `#5A5A5C`.

### Forms

- Input border: 1px `#D6D8DD` soft gray.
- Input border on focus: 1px `#014D75` Mission blue.
- Input radius: 4px.
- Input padding: 14px 16px.

---

## 10. Logo

The Mission Hygieia logo (the existing wordmark/icon used on missionhygieia.org) appears in the top-left of every page nav and in the footer.

### File path

The site looks for `logo.png` in the root folder. Save the official logo there. Until then, a typographic fallback in Lora handles the slot.

### Sizing

- **Nav lockup:** 36px tall.
- **Footer:** 40px tall.
- **Favicon:** Inline SVG mark.

### Acceptable backgrounds

White (`#FFFFFF`), soft white (`#F7F8FA`), or solid Mission blue (`#014D75` — use a single-color white version of the logo on this background).

### Forbidden

No drop shadows. No outlines. No rotation, stretching, recoloring outside approved versions.

---

## 11. Accessibility

- **Color contrast:** Body text on background must be at least 4.5:1 (WCAG AA).
- **Tap targets:** 44×44px minimum on mobile.
- **Focus states:** Every interactive element gets a visible focus ring — 2px `#B85528` rust outline, 2px offset.
- **Alt text:** Every image gets descriptive alt text. Decorative-only illustrations get `alt=""`.
- **Heading order:** One h1 per page. Don't skip levels.

---

## 12. What to do when you're not sure

The decision tree, in order:

1. Does this serve a donor, volunteer, or shelter director's actual question? If not, cut it.
2. Does it make us look like a peer of Charity:Water or ProPublica? If not, change it.
3. Could this be quieter, smaller, or use less color? If yes, do that.
4. If you're still unsure, do nothing. Whitespace is always a defensible choice.
