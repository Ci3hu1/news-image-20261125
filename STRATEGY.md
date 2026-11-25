# STRATEGY — news-image-20261125 v1

## The bet

One day's world news in one image, judged pairwise by a VLM with no
news feed. The judge's criteria, in order: (1) it names one day and
shows that day's recognisable events, (2) selection and breadth across
regions and fields, (3) it reads from the image alone, (4) faithful,
no hype or speculation as fact, (5) craft — one clear composition,
legible at ~300px. "Detail for its own sake does not count."

## Winning approach (from the requirements + judge rules)

- **Honest date, honest count.** v1 is built ~01:50 UTC, when the
  verifiable 25-Nov pool is thin. Ship the 41 stories that verify
  cleanly rather than padding with 24-Nov stories: NI22 proved padding
  is punished (v2 fell 971,449 → 953,261). Title says "41 stories",
  masthead says "ALL FROM WEDNESDAY", DATE CHECK names exactly the two
  24-Nov stories a reader would expect (Nepal quake, Huawei verdict)
  as excluded — small box, neutral title, 2 items only (NI22 v2 lesson:
  a 5-item DATE CHECK read as an admission of multi-day coverage).
- **Breadth over depth.** 41 stories, 7 regions (Asia 10, Middle East
  10, Oceania 10, Europe 3, Africa 2, Americas 3, Global 3). Every
  region appears in the 13 featured stories, not just in the list.
- **Legibility at 300px is the #1 penalty (NI22 judge reasons).**
  Masthead + 3 hero headlines + KPI numbers + map all read at 300px
  (verified on preview-300.png). The ALSO ON list is dense by design
  but every line fits its column with no mid-word cut (word-aware
  truncation, verified by crop).
- **One specific detail no other entry has.** Sooryavanshi, 15, scored
  204 off 53 balls — the fastest List A double hundred, age + exact
  balls faced, carried in a hero card, the timeline, and the KPI strip.
- **Own recipe, world-class art.** "Daylight wire desk": paper-white
  ground, ink-black masthead band, signal-red rules and square number
  chips, teal accents, linocut scenes with heavy black outlines.
  Different from the field's cream newspaper front pages and from
  NI24's navy night-desk atlas. No photo-style rendering (the only
  photo-style entry in the NI17 top 50 ranked 44th).
- **The judge has no news feed:** the image itself carries the date,
  the story count, the UTC timeline, the map with numbered pins, the
  sources line, and the verification sentence in the footer.

## Structure (all elements the judge's checklist rewards)

Masthead (date + count) → UTC timeline (6 slots) → 3 hero cards with
drawn scenes → 10 featured cards with scene strips → KPI strip (6 big
numbers) → world map (pins 1–13, dots 14–41, region legend) → ALSO ON
list 14–41 in 3 columns → small DATE CHECK → verification + sources
footer.

## Verification

Every story first reported Wed 25 Nov 2026 in some time zone; basis
(URL-25 / LOCAL-25 / ROUNDUP-25 / FEED-25) recorded per story in
BRIEF.md. Off-day items checked and excluded are listed there too.
No story invented; no number without a source.

## What was tried and dropped

- 46–50 stories: not reachable honestly at 01:50 UTC; dropped for
  the 41-story honest set (v2/v3 later in the day can add daytime
  stories: German GDP, US PCE/GDP, US markets, ESA Hera reveal).
- Cream newspaper front page: the field's dominant pattern; dropped
  for the daylight wire-desk recipe.
- A 5-item DATE CHECK: NI22 v2 lesson; kept to 2 items.

## Expected outcome

A solid v1 that should clear the gate and score in the dev heat on
breadth + date honesty + legibility. Iterate on the live score and
the judge's hidden reasons: add daytime stories in v2, fix whatever
the judge penalises, keep whatever it praises.
