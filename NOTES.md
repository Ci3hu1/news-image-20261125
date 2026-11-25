# NOTES — news-image-20261125 v1 (early edition)

- Built: Wed 25 Nov 2026, ~08:31–09:00 WIB (01:31–02:00 UTC), by subagent.
- Bounty: "Sum up 25 November's world news in one image", $100, 50 paid
  places ($20/$12/$6, then $2/$1.20). Entries opened 25 Nov 07:00 WIB;
  entries close 27 Nov 07:00 WIB; results 11 Dec 2026.
- Quota at build: day cap 6, left 6, can_submit true. Field at build:
  67 submissions (competition API, 25 Nov ~08:24 WIB); early leader
  972,121 (quiet-panda-11).
- v1 = EARLY EDITION: 41 stories, 7 regions (EUROPE 3, MIDDLE EAST 10,
  ASIA 10, AFRICA 2, AMERICAS 3, OCEANIA 10, GLOBAL 3). Every story
  verified as first reported Wed 25 Nov 2026 in some time zone;
  verification basis per story in BRIEF.md. The two biggest 24-Nov
  stories (Nepal 5.6 quake, Huawei guilty verdict) appear ONLY in the
  2-item DATE CHECK as excluded.
- Visual language: "daylight wire desk" — paper-white ground, ink-black
  masthead band, signal-red rules and square number chips, teal
  accents, linocut scenes with heavy black outlines. NOT the cream
  newspaper front page the field copies, NOT NI24's navy night-desk
  atlas. 3 heroes + 10 illustrated cards + KPI strip + map with
  numbered pins 1–13 + dots 14–41 + ALSO ON list (3 columns) +
  DATE CHECK + sources.
- One specific detail: Sooryavanshi, 15, scored 204 off 53 balls
  (fastest List A double hundred) — in a hero card, the timeline,
  and the KPI strip.
- Render: 1024x1024 RGB PNG, 320,464 bytes, sha256
  e0712f34fc089eaad90fecf69bc2036c4443506543e5de0dc111a55417c2c08e.
  Byte-deterministic across two renders. Sharpened (UnsharpMask r2,
  150%). preview-300.png included; masthead + 3 hero headlines + KPI
  numbers read at 300px.
- Tests: 6/6 pass (python3 -m unittest discover -s tests), incl.
  determinism (main.py twice byte-identical), clearance 0, main.py
  stdlib only, main.py runs as uid 65534 on a read-only repo copy
  and writes byte-identical output mode 0644.
- Visual fixes applied (2 rounds): (1) timeline events truncated by
  fit_lines — shortened all 6 event strings to fit one line; ALSO ON
  titles shortened to fit 3 columns; scene text labels ("204",
  "SORRY", "$") gated to hero-size scenes only; map pins staggered
  where cities share coordinates (Delhi/Chandigarh, Gaza/Sanaa/Doha,
  Canberra x2); ALSO ON font 12px → 11px with word-aware truncation.
  (2) item 29 truncated ("— …") — title shortened to fit.
- main.py: pure stdlib, copies bundled entry.png to
  $MAKEFUN_OUTPUT_DIR/entry.png (else /output/entry.png, else
  output.png), chmod 0644.
- Lessons applied from NI22: 41 verified stories instead of padding
  to 50 with off-day stories (v2 fell 971,449 → 953,261 on that);
  DATE CHECK small (2 items) and neutral; no number without a source;
  pins staggered; future events (US PCE/GDP, Hera reveal) kept out of
  the story list except the scheduled Hera reveal in the timeline.
- NOT submitted. Submit needs Joni's 'Setuju' on the exact entry.
- Next: v2/v3 later in the day add verified daytime stories (German
  GDP, US PCE/GDP, US markets, evening wires, Hera close-ups) before
  entries close 27 Nov 07:00 WIB. Read the judge's hidden reasons
  after the live score before building v2.
