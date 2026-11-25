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

## Bundle + check — 25 Nov 2026 ~09:02–09:03 WIB (subagent e6da46a7)
- Kit: fresh download for this bounty (skill guide 1.5.285).
- Bundle --dry-run first: 18 session files found; 13 pre-opening
  (23 Nov) sessions auto-excluded by the kit (thinking_in_window).
- Bundle failed twice before succeeding: (1) --parent-session rejected
  — the parent session is already carried as evidence, never pass it
  as parent; (2) run record incomplete — fixed with --prompt-file
  ~/workspace/tools/makefun/ni25-prompt.txt (cron job body verbatim,
  the schedule's configured prompt), --prompt-origin scheduled,
  --prompt-via "cron makefun-cek-bounty-baru-rutin (30-minute
  make.fun bounty check)", --mcp none, --harness muse-app
  --harness-version 1 --provider ipnext --model
  ipnext/avocado-5.17-v2 (model id from agent.agents, not renamed).
- Usage: muse.db SELECT on agent_message_token_usage returned 1 row
  (parent agent 9de7d04e, message b4db4330, 909,270 in / 14,580 out,
  model ipnext/avocado-5.17-v2) → ~/.makefun/muse-usage-ni25.jsonl.
  Builder subagent's own row is written only when its run completes,
  so it is NOT in this bundle — the kit's own warning says the
  top-level agent must re-run the SELECT (parent + subagent ids) and
  re-bundle before submitting, to attach the builder's row.
- Bundle: ~/workspace/tools/makefun/bundles/ni25-bundle.tar.gz
  (1,280,792 bytes, sha256
  4dd7079e4815ac7a898c650a0caf8a422b386ed40ea8aeaa0291cdaa90d42b2b),
  18 sessions.
- Kit check: ok — 13 passed, 0 failed, 6 skipped, 5 checked at
  submission. thinking_in_window PASS, thinking_reproduces PASS
  (46.6% authored), thinking_priced PASS (1 usage record),
  transcripts_run_record PASS. thinking_own_work SKIP (note only):
  sessions fetched another entry's status route
  (make.fun/api/submissions/01a20c43-…/status) — reference only,
  never a rejection.
- At-submission checks (site's, not check's): repo_public,
  repo_owner (.makefun/owner.json or submit from the GitHub-owner
  account), repo_created_after_open, commit_in_repo,
  duplicate_snapshot. Repo is public, commit 977b2e55 pushed.
- Commit 977b2e55b00e1ba1ebd68518794330ac1b0b6e14. READY for Joni's
  'Setuju'. Do NOT submit.

## Submission — 25 Nov 2026 ~10:20 WIB (on Joni's "Setuju, submit NI25 v1" 10:09 WIB)
- Joni approved the exact entry (commit 977b2e55) at 10:09 WIB.
- Re-bundle before submit: usage file gained the builder's row
  (e6da46a7, message 4f396aa0, 13,944,175 in / 68,235 out) + a second
  parent row (427e247e); 3 rows total, all attached.
- First re-bundle (ni25-bundle-v2.tar.gz, discovery) FAILED kit check
  on thinking_in_window: discovery pulled in 24 sessions incl. the
  main-agent session 2d7fced3 with 100 pre-open timestamps. Fix:
  re-bundled with --no-discover + the exact 18 sessions from the v1
  bundle → ni25-bundle-v3.tar.gz (973,801 bytes, sha256
  5162a7801aeb6ca11d58339a51ea38d6444f300cb4dc735af89460b697f8af2b),
  kit check ok=true, failed=[] (13 pass, in_window PASS,
  reproduces 46.6%, priced 3 records).
- Submission: 01a210b7-89ad-7631-a2b8-b5199fc221a0, stage submitting at
  submit (round 1), title "Daylight wire desk — 41 stories from
  25 November 2026". Live status right after submit: preparing, no
  scores yet (blind rounds — no live score until results).
- Claim code saved to ~/.config/makefun/news-image-20261125-submission.json (0600).
- Live score/rank: none yet (blind rounds). Next: v2 later in the day
  with daytime stories; read judge's hidden reasons after the live
  score before building v2.
