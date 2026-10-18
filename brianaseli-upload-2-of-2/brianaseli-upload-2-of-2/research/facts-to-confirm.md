# Facts to confirm with Brian

Nothing on this list is on the live site. Each item names what to send and what changes once it is confirmed. To publish an entry after confirmation, set `"publish": true` (and update `"verification"`) in `data/media-library.json` — see `HANDOVER.md`.

## A. Decisions only Brian can make (blocking launch)

| # | Decision | Why it matters | Site default today |
|---|---|---|---|
| 1 | **Contact details for public use** — +254 724 000 741 and brianaseli26@gmail.com | Taken from his own bio and booking poster. Confirm they are the booking line, not a personal number. | Shown (from his own materials) |
| 2 | **Is the number on WhatsApp for bookings?** | WhatsApp is the fastest Kenyan booking channel. | WhatsApp button off (`site.json → contact.whatsappEnabled`) |
| 3 | **Enquiry destination** — email only, form service (Formspree / Web3Forms), Netlify Forms, or a CRM | The form must deliver to a real inbox. | Opens the visitor's email app pre-filled to brianaseli26@gmail.com |
| 4 | **Budget question on the form** — include or not? | Qualifies leads but can put off some clients. | Off (`site.json → form.showBudget`) |
| 5 | **Domain** — is brianaseli.me.ke his? Preferred domain? | Canonical URLs, sitemap and social previews use it. | `https://brianaseli.com` placeholder in `site.json` |
| 6 | **Employer policy** — does NMG need to approve outside engagements or name use? | Brief requires independence from the employer. | Footer disclaimer in place |
| 7 | **Services currently offered** — speaking, creative direction, content development, broadcast hosting? | Bio lists them; confirm they are open to bookings. | All shown, with broadcast work "subject to employer policy" |

## B. Engagement credits (timeline graphic)

For each: confirm the role (MC / host / moderator), whether it was an **independent booking or an NMG duty**, and send one piece of evidence (organiser post, programme, photo showing event branding).

- [ ] 6th Annual SME Conference & Expo — KICC Courtyard, 26–28 Mar 2025 (NMG)
- [ ] Nation–Huawei LEAP Job Fair — University of Nairobi, Jul 2025 (NMG/Huawei) — also confirm "60+ companies"
- [ ] Higher Education Fair & Skills Expo — Sarit Centre, Jan 2026 — organiser?
- [ ] 5th International Women's Day Forum "Give to Gain" — Mövenpick, Mar 2026 — organiser?
- [ ] 14th Annual Media Excellence Awards — Safari Park Hotel, 15 May 2026 (MCK)
- [ ] Skill Up Africa 4th edition — KICC, 15–16 Jul 2026 (NMG)
- [ ] Nation Digital Summit CEO Roundtable — Aug 2026 — moderator?
- [ ] SunDev East Africa Swing — Aug 2026 — is this the Sunshine Development Tour? Which event?
- [ ] 3rd Annual Media–CSO Conference — the 2nd was in Nov 2024; is the 3rd in Nov 2026 (upcoming) or did it happen in 2025?
- [ ] Daystar University 48th Graduation (14 Nov 2025) — any role?
- [ ] Any other corporate/institutional engagements (client name approval needed for each)

## C. Awards and credentials

- [ ] Kenya Theatre Awards: OK to use official wording "Best Musical Arrangement/Score/Adaptation — *Jaboya*" instead of "Music Director of the Year"? *(Site uses official wording.)*
- [ ] Star of Excellence Award (2017) — awarding body, document or link
- [ ] Daystar Alumni of the Year (2017) — document or link
- [ ] Standard Media Most Promising Star (2016) — context (press says he joined Standard in 2017)
- [ ] National Drama Festival best performing male artiste (2009) — include?
- [ ] BA Communication (Electronic Media), Daystar University — year
- [ ] Diploma in Performing Arts & Public Relations, East African Media Institute — year *(education is shown on About as stated in his bio — confirm)*

## D. Current roles and claims

- [ ] *Vibe Shift* (Nation FM) and *Friday Night Rave* (NTV) still current as of launch? Slots unchanged?
- [ ] "More than 5,000 interviews" (from his July 2023 Instagram post, reported by Pulse) — OK to publish as his own figure? Recommended: yes, attributed.
- [ ] "More than one million viewers weekly" for Youth Café — source? *(not published)*
- [ ] Theatre credits — role on each: *Sarafina*, *Gor Mahia*, *Lovestruck*, *Jaboya*, *Lich*, *Fragments*; *Chebet* in development. Writer, director, music director? *(only Jaboya shown, via the award)*
- [ ] Redfourth Chorus — still associate director?
- [ ] "Working with Brian" process (brief → run-of-show → prep → rehearsal → on the day → wrap) — matches how he works?

## E. Media, rights and permissions

- [ ] **Videos now on the site** — confirm Brian is happy with each: NTV *Creatives & Coins* interview; *What's On Your Shelf?* interview; *The Hot Seat KE* promo; KTN Entertainment spoken-word surprise (2019); breakfast-radio prank clip "This is how Brian Aseli got played" (2023); KTN *Youth Café: Art Corner* (2017); Muhanjii *Youth Café* feature (2017). Any can be removed by setting `"publish": false`.
- [ ] **Stage background images** supplied for the redesign — confirm they're licensed for commercial use (several look like stock/template images; two came with visible watermarks and were not used).
- [ ] **Cut-out portraits**: approve the background-removed versions used in the hero (including the green-suit photo from the bio cover).
- [ ] **Event photos now on the site, needing the owners' permission before launch:** Kenya Theatre Awards 2023 hosts photo (The Theatre Times); KITFEST 2024 launch stage photo (Kenya Cultural Centre newsletter); *Jaboya* cast photo (Business Daily, "PHOTO | POOL"). Each is credited on the page. If permission isn't given, replace them with Brian's own event photos.
- [ ] **On-stage microphone photo** (sequinned jacket) is cropped from the booking-poster graphic. Confirm it's an original photograph and who took it.
- [ ] **YouTube thumbnails** are saved locally so they load fast and offline. They belong to each channel; showing them alongside a link to the video is standard practice, but confirm Brian is comfortable with each.

- [ ] **Showreel** — does one exist? If not, recommended: a 60–90 second cut from two or three events plus a broadcast moment.
- [ ] Facebook Reel `facebook.com/share/r/1FcShnbnG1` — what is it, is it public, can it be embedded?
- [ ] Photographer credit and usage rights for the DON-series studio portraits
- [ ] Event photo `IMG_0716` (Spotify Quiz Night backdrop visible) — event name, OK to publish, photographer credit
- [ ] Bio-cover and leather-jacket photographs — photographer credit and rights
- [ ] Testimonials — any organisers willing to be quoted by name and organisation? *(Testimonials section stays hidden until at least one approved quote exists.)*
- [ ] Personal topics discussed in interviews (e.g. in the Creatives & Coins episode) — site copy does not reference them; confirm he is comfortable with the episode being featured.
- [ ] Two LinkedIn profiles exist — which is current? (`brian-aseli-a724921b0` is used on the site)
- [ ] X / TikTok / YouTube handles to add to the footer?
