# Brian Aseli website — handover

A fast, static website built with [Astro](https://astro.build). No database, no server to maintain, no tracking. All content lives in four plain data files.

## Quick start

```bash
npm install
npm run dev        # local preview at http://localhost:4321
npm run build      # production build into dist/
npm run check      # broken links, missing metadata, leaked unverified entries
```

Requires Node 20+.

## Where everything lives

| What | File |
|---|---|
| Contact details, social links, showreel, form settings, testimonials, disclaimer | `data/site.json` |
| Services copy | `data/services.json` |
| Bios (programme intro, short, full) | `data/bios.json` |
| Every credit, award, interview and press item — with verification | `data/media-library.json` |
| Photographs used on pages | `src/assets/photos/` (prepared by `scripts/prepare-photos.py`) |
| Press portraits (downloads) | `public/downloads/portraits/` + thumbnails in `src/assets/press/` |
| Media kit PDF, share image, touch icon | built by `scripts/build_media_kit.py` |
| Research audit, register, open questions | `research/` |
| Brand strategy, content architecture | `docs/` |

## Common updates

### Publish a newly confirmed engagement
1. Open `data/media-library.json` and find the entry (e.g. `lead-nation-digital-summit-2026`).
2. Update `role`, `displayDate`, `url` (the evidence link), `summary`, `demonstrates`.
3. Set `"verification": "verified"` (or `"partial"`) and `"publish": true`.
4. Optionally set `"featured": true` to surface it on the homepage.
5. `npm run register` (refreshes `research/source-register.csv`), then build and deploy.

It will appear automatically on Engagements, Work, the homepage credits (if among the newest three), any matching service page (via `tags`: `corporate`, `mc`, `moderation`, `entertainment`, `broadcast`, `creative`, `theatre`, `institutional`), and the next media kit build.

**Rule of thumb:** if there is no link or document you would be comfortable showing a client, leave `publish` false.

### Add an interview, article or video
Copy an existing `media` entry, give it a unique `id`, fill the fields, set `publish: true`. For YouTube, add `"youtubeId"` and `"format": "embed-video"` — it plays in privacy-enhanced mode and only loads when pressed.

### Add the showreel
Upload to YouTube (public or unlisted), then in `data/site.json`:
```json
"showreel": { "youtubeId": "ABC123xyz", "title": "Brian Aseli — Showreel", "description": "Two minutes across stages, studios and conversations.", "uploadDate": "2026-11-01" }
```
The hero button changes to **Watch the showreel** and the Work page leads with it.

### Add a testimonial (only with the person's written approval)
```json
"testimonials": [{ "quote": "…", "name": "Jane Wanjiru", "role": "Head of Events", "organisation": "Example Bank" }]
```
The section appears on the homepage once there is at least one.

### Light and dark mode
The site follows the visitor's system setting; the sun/moon button in the header switches it and the choice is remembered on that device. Colours live in `src/styles/global.css` (`:root` for light, `[data-theme='dark']` for dark). Stage sections (`.stage`) stay dark in both modes.

### Cut-outs (Brian placed under stage light)
The hero and page headers use photos of Brian with the background removed (`source-photos/cutouts/*.png`). To make a new one from a portrait:
```bash
mkdir bgr && cd bgr && npm init -y && npm i @imgly/background-removal-node
# then run scripts/cutout.mjs from the project: node ../scripts/cutout.mjs ../source-photos/NEW.jpg=newname
```
Put the PNG in `source-photos/cutouts/`, run `python3 scripts/prepare-photos.py`, then register it in `src/lib/photos.ts` under `cutouts`. Check the edges at full size before publishing — hair and hands are where cut-outs go wrong.

### Stage backgrounds
`source-photos/stage/*.jpg` are the lighting images supplied for the brand. `prepare-photos.py` enlarges and cleans them. They are decorative only (empty alt text). Each has a focal point in `stagePos` in `src/lib/photos.ts`. Please confirm these images are licensed for commercial use — some look like stock or template backgrounds.

### Hero slides
Edit the four slides (headline, line, photo, background) at the top of `src/components/HeroActs.astro`.

### Video thumbnails
Thumbnails are saved locally in `source-photos/thumbs/aseli-yt-<VIDEO_ID>.jpg`. Add one for any new video (download `https://i.ytimg.com/vi/<VIDEO_ID>/maxresdefault.jpg`), then run `python3 scripts/prepare-photos.py`. Without a local file, the card falls back to loading the thumbnail from YouTube.

### Event photos on credits
Put the photo in `source-photos/events/<name>.jpg`, run `python3 scripts/prepare-photos.py`, then set `"image": "<name>"` and `"imageCredit"` on the entry in `data/media-library.json`.

### Videos
Any entry in `data/media-library.json` with a `youtubeId` and `"publish": true` appears in the video carousels and plays in the site's own player. `videoGroup` (`conversations` or `on-air`) decides which carousel on the Watch page; the order is set in `videoOrder` in `src/lib/data.ts`.

### Replace or add photographs
1. Put originals in `source-photos/`.
2. Add it to the `portraits` list in `scripts/prepare-photos.py`, then run `python3 scripts/prepare-photos.py`.
3. Register the new key, file and alt text in `src/lib/photos.ts`.
Never use stock images of other people, generated images of Brian, or employer-branded artwork.

### Rebuild the media kit PDF after content changes
```bash
pip install playwright && playwright install chromium
python3 scripts/build_media_kit.py
```
It reads the same data files, so it never claims more than the site.

## Configure the enquiry destination

Edit `data/site.json → form`:

| Mode | Setup | Behaviour |
|---|---|---|
| `"mailto"` (current) | none | Opens the visitor's email app, pre-filled to `contact.email`. Page says clearly nothing is sent until they press send. |
| `"endpoint"` | Create a form at Formspree / Web3Forms / your CRM webhook. Put its URL in `form.endpoint`, or set the environment variable `PUBLIC_ENQUIRY_ENDPOINT` in your host. | Submits in the background; shows success only if the service confirms. |
| `"netlify"` | Host on Netlify; enable Forms. Set email notifications in Netlify → Forms. | Netlify captures each enquiry. |

Turn on the WhatsApp button with `contact.whatsappEnabled: true` once the number is confirmed for WhatsApp bookings. Turn on the budget question with `form.showBudget: true` (edit `budgetBands` as needed).

After switching modes, send a real test enquiry and confirm it arrives before announcing the site.

## Deploy

The build output (`dist/`) is plain static files and runs on any host.

**Vercel or Netlify (recommended):**
1. Push this folder to a GitHub repository.
2. Import it in Vercel/Netlify. Build command `npm run build`, output directory `dist`.
3. Add environment variable `SITE_URL` = the final domain (e.g. `https://brianaseli.com`). This sets canonical URLs, sitemap and share previews.
4. Add the custom domain and its DNS records as the host instructs.
5. After the first deploy: open every page, submit a test enquiry, paste the URL into a WhatsApp/LinkedIn post preview to check the share card, and submit `/sitemap-index.xml` in Google Search Console.

**Domain note:** a site at `brianaseli.me.ke` already exists in search results — confirm whether Brian owns it before choosing a domain. The current placeholder is `https://brianaseli.com`.

## Search and discovery — next steps

- Put the site URL in the bio of Instagram, LinkedIn, Facebook and X, and in every email signature.
- Ask organisers who credit Brian to link to the site, not just tag him.
- Attach the media kit PDF to proposals; it carries the contact details and the site's credits.
- Keep `media-library.json` current — fresh, sourced credits are the strongest signal for both search engines and buyers.
- No ranking or AI-citation outcome can be guaranteed; the site is built to make the facts easy to find and verify.

## Independence safeguards (keep these)
- The footer disclaimer (`site.json → disclaimer`) and the broadcast-service note.
- No employer logos or programme artwork.
- Events organised by Brian's employer stay unpublished until he confirms they were independent bookings.
