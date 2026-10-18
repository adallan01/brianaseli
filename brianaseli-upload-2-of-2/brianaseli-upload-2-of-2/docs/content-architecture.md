# Content architecture

## Sitemap

| URL | Purpose | Primary action |
|---|---|---|
| `/` | Establish value in one screen; prove it; route to services, media and booking | Book Brian |
| `/about/` | Editorial story, how he works, sourced milestones, copy-ready bios | Check availability |
| `/services/` | Six services: need → role → what he brings → outcome, with linked credits; "Working with Brian" process | Enquire about [service] (pre-fills the form) |
| `/work/` | Featured video (showreel slot), photographs, filterable list of every published credit and appearance | — |
| `/engagements/` | Documented event credits and awards (filterable); on-air record table | Send credit details (organisers) |
| `/media/` | Featured interview; searchable, filterable press archive | — |
| `/media-kit/` | PDF download, fast facts, bios, approved portraits | Download media kit |
| `/contact/` | Booking enquiry form + direct phone/email | Send enquiry |
| `/privacy/` | How enquiry data is handled | — |
| `/404` | Recovery | Back home / enquire |

Also generated: `/sitemap-index.xml`, `/robots.txt`, Open Graph image, Person / Service / VideoObject structured data.

## Homepage sequence

1. **Hero** — eyebrow *The Most Bankable Host*; headline *He reads the room. Then he leads it.*; supporting line; **Book Brian** + **See Brian in action** (switches to **Watch the showreel** when `site.json → showreel.youtubeId` is set); "Based in Nairobi · Available across Kenya and Africa"; role strip.
2. **Proof strip** — four sourced facts (since 2017 on national TV/radio; daily live radio on Nation FM since 2023; Kenya Theatre Awards 2024; KTA 2023 co-host + KITFEST 2024 MC).
3. **Why clients book him** — "What you're really booking is judgement": broadcast discipline, conversation craft, stage instinct; event photograph with Brian's own quote.
4. **Services range** — tabbed discovery (keyboard accessible), each tab linking to the full service section.
5. **Watch, read, listen** — featured NTV interview + two featured press items; link to archive.
6. **Selected credits** — newest three documented credits, each with its source link.
7. **Testimonials** — renders only when `site.json → testimonials` has approved entries.
8. **Footer CTA** — sign-off, proposal request, media kit.

Calls to action appear in the header, hero, each service, and the footer — never more than one primary CTA per screen.

## Credit types (never mixed up)

Every card carries a badge: **Event credit** (an engagement he hosted), **Award**, or a media type (**Press**, **Podcast**, **Interview**, **Broadcast clip**). A TV appearance is never presented as an event booking.

## Booking flow

1. Visitor clicks any "Book" / "Enquire" CTA → `/contact/` (service pre-selected when coming from a service section).
2. Form: name, organisation, work email, telephone, event name, date (past dates blocked), event type, service, venue, audience size, languages, optional budget (off by default), brief, consent.
3. Validation: inline messages, focus moves to first error, error lines reserve space so the layout doesn't jump; honeypot + minimum-time spam guards.
4. Delivery (set in `data/site.json → form.mode`):
   - `mailto` (default) — opens the visitor's email app with the enquiry written out; the page states plainly that nothing is sent until they press send, and offers a copy-to-clipboard fallback.
   - `endpoint` — POSTs JSON to a form service (Formspree, Web3Forms, a CRM webhook); success is shown only on a 2xx response; failures say "not sent" and keep the data.
   - `netlify` — Netlify Forms, when hosted on Netlify.
5. "What happens next" panel sets expectations without promising a response time.

## Media archive structure

`data/media-library.json` is the single source. Each entry carries: title, type, section (`engagement` / `award` / `media` / `career`), category (used for filters), platform, publisher, URL, original publisher, publication and event dates, display date, Brian's role, summary, what it demonstrates, evidence, verification status, conflict notes, `publish`, `featured`, presentation format, YouTube ID, rights notes, and service tags (which link credits to service pages automatically).

## Held back pending Brian's confirmation

See `research/facts-to-confirm.md`. Notably: the nine timeline-graphic events, the 2016–2017 awards, theatre roles per production, the "5,000 interviews" figure, Youth Café reach, testimonials, the showreel, the Facebook Reel, WhatsApp and the enquiry destination.
