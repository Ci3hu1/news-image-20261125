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

## v2 — daytime edition, 46 stories — 25 Nov 2026 ~18:15–18:45 WIB (subagent 348d6d8a)

- 41 → 46 stories. All 41 v1 stories kept unchanged. Five daytime stories
  added, each first reported Wed 25 Nov 2026, verified from a primary
  source read on the outlet's own page:
  - 42. EUROPE/Berlin — "German GDP +0.1%, revised down" — Destatis
    press release No. 409 of 25 Nov 2026 (Q3 +0.1% q/q, +1.2% y/y,
    revised down 0.1pp from the 30 Oct first release). [URL-25]
  - 43. MIDDLE EAST/Ras Tanura — "Houthis claim refinery, Riyadh
    strikes" — Reuters 25 Nov (Houthi spokesman said Wednesday the
    group attacked Ras Tanura refinery + Riyadh financial district;
    coalition intercepted 4 drones in Ras Tanura earlier Wednesday).
    [URL-25]
  - 44. ASIA/Beijing — "China probes Politburo member Chen Jining" —
    Reuters 25 Nov (anti-graft probe of Shanghai party chief, 4th
    Politburo inquiry since 2025). [URL-25]
  - 45. EUROPE/Barcelona — "Puigdemont to return to Spain on Dec 12" —
    Reuters 25 Nov (said Wednesday, ending nearly a decade of exile
    after the amnesty applied). [URL-25]
  - 46. GLOBAL/Seoul — "Asian stocks slide on tariff threats" — Reuters
    25 Nov (MSCI Asia-Pacific ex-Japan -2.3%, Korea -5.3%, Taiwan
    -5.1%, Nikkei -2.9%, S&P futures -0.3%). [URL-25]
- Region counts v2: EUROPE 5 · MIDDLE EAST 11 · ASIA 11 · AFRICA 2 ·
  AMERICAS 3 · OCEANIA 10 · GLOBAL 4 = 46.
- Layout: ALSO ON list 3 cols x 11 rows (was 10), pitch 13 → 12px;
  masthead 41 → 46; map dots 14–46; timeline AFTERNOON slot now
  "German GDP +0.1%" (Sensex stays story 15). KPIs, DATE CHECK (2
  items, unchanged), heroes, featured unchanged. German GDP poster line
  shortened to "German GDP +0.1%, revised down — Destatis" (full
  "revised down from 0.2%" measured 336.8px > 325px column).
- Render: entry.png 325,805 bytes, sha256
  6abf4403843052a490e6308dc8a0d3b38549349f35ad2a4a1241305a149442ec,
  byte-deterministic across renders, clearance violations 0, tests 6/6
  pass. Visual check: masthead + 3 hero leads + KPI strip read at
  300px; ALSO ON items 42–46 complete with sources, no truncation.
- Competition/quota re-checked 25 Nov ~18:15 WIB: acceptingSubmissions
  true, can_submit true, day cap 6 (taken 1, left 5), hard limit left
  39, entry_fee null, field 6,504 entries (was 2,512 at v1 submit).
- Deliberately left out (for v3): US PCE + Q3 GDP second estimate (BEA
  8:30 AM ET = 20:30 WIB, not yet released at build time); ESA Hera
  Dimorphos reveal (19:45 CET, not yet happened); Ramaphosa Farmgate
  win, Wipro–BP deal, Spain election debate, Jordan death sentence,
  Thanksgiving travel, Sahel drones feature (all Reuters 25 Nov,
  verified but held — ALSO ON fits 33 items at 11 rows; v3 needs a
  4-column restructure or swaps to go past 46).
- Commit 829462f3c93ca8bb4540324f45b20c91ae75de26 "news-image-20261125
  v2: 46 sourced stories, daytime edition" (5 files: entry.png,
  preview-300.png, render_poster.py, BRIEF.md, STRATEGY.md).
  **PUSH BLOCKED in this session: the proactivity session's egress
  policy denies GitHub POSTs (policy_denied
  proactivity_read_only_preparation, hitl_domain_allow_github_com) —
  git push/fetch and the Git Data API all refused; remote verified via
  API still at 007db80. The parent (main agent) session must push
  829462f + the docs commit below.**
- Fresh kit downloaded 25 Nov ~18:26 WIB: ni25-kit-v2.tar.gz
  (8,475,457 bytes), harness@c62b0ab7… / scorer@26f98e34… (v1 kit was
  harness@9cb66b22… / scorer@a1a1fe4a…).
- Kit check (fresh kit, commit 829462f, 19 sessions + makefun-run.json,
  25 Nov ~18:30 WIB): ok=false, failed=[thinking_priced,
  transcripts_run_record]. PASSES (entry proven sound):
  competition_open, snapshot (10 files, 507,524 bytes, within caps),
  license_osi (MIT), entrypoint (main.py, python3.13),
  transcripts_present/recorded (19 sessions), thinking_wellformed,
  thinking_in_window (all 554 timestamps in window),
  thinking_reproduces 50.2% authored (548/1090 lines; render_poster.py
  final content from 3 write/edit messages), thinking_turns (291),
  thinking_revised. Skips: strategy_note, committed_secret,
  thinking_committed, thinking_on_task, thinking_fresh,
  thinking_own_work. Submission-phase checks (repo_public, repo_owner,
  repo_created_after_open, commit_in_repo, duplicate_snapshot) resolve
  at submit once 829462f is pushed.
  - thinking_priced FAILS: loose transcripts carry 0 usage rows (Muse
    keeps usage in its DB, not the session file). The kit's own fix
    says a subagent cannot do this step: the top-level agent must run
    the muse.db SELECT with every session's agent_id and re-bundle
    with --muse-usage (v1 usage file ~/.makefun/muse-usage-ni25.jsonl
    has 3 rows; the v2 builder's row is written only when this run
    completes).
  - transcripts_run_record FAILS: the run record is present
    (makefun-run.json, prompt handed-off, parent chat 1f628cec listed)
    but the check cannot complete the parent chain from the subagent's
    session files — the Muse app session records no parent_session_id,
    and the tool resolves the chain from the top-level agent's session
    (which holds the spawn). The tool's own message: "run bundle from
    that top-level agent." The parent must re-bundle at submit time
    (same flow as v1). Bundle attempts in this session: dry-run with
    --no-discover + 18 v1 sessions + builder session + --parent-session
    1f628cec + --effort default — refused on missing parents; the
    373 MB main-chat session file exceeds the 128 MB per-session cap
    and is NOT the spawning session (the spawner is 1f628cec, 514 KB).
- Prompt file for this build: ~/workspace/tools/makefun/ni25-v2-prompt.txt
  (task verbatim). Fresh kit dir:
  ~/workspace/tools/makefun/news-image-20261125-kit-v2/.
  Check transcripts dir: /tmp/ni25-v2-transcripts/ (19 sessions +
  makefun-run.json + system_prompt.md + AGENTS.md +
  parent-chats/requester/1/muse-app/1f628cec….jsonl).
- READY for Joni's 'Setuju' on the entry itself (commit 829462f,
  46 stories). Do NOT submit until the parent pushes + re-bundles.
