# Course Template — Design Snapshot

Canonical project memory. Read this first each session. (Plans in journey/plans/, logs in
journey/logs/, research in journey/research/.)

## Strategy

Minimal-dependency, content-driven course site: authors edit Markdown, everything else is
automatic. Chinese (`zh-CN`) university course. Astro website + Slidev decks, both deployed
as a single static `site/`.

## Key design decisions

- **Two content stores**: `src/` (plain Markdown, no frontmatter, draft source) and
  `website/src/content/` (Markdown + YAML frontmatter, what Astro consumes). Manual sync
  between them; no automation script (by design — keep it simple).
- **Slide decks mirror the site**: `site/slides/lectureN/` holds built decks, linked from
  the homepage via `slidevUrl` (rendered as `base + slidevUrl`).
- **Root build workflow** (added 2026-09-11, see journey/plans/2026-09-11-build-workflow.md):
  - `astro build` clears `website/dist/` by default (emptyOutDir) → website sync is always
    a full regenerate + full mirror into `site/` (empty first).
  - Slide decks build incrementally (mtime-based) into `slides/dist/lectureN/` cache, then
    copied to `site/slides/lectureN/`. `--force` rebuilds all.
  - Deck base = `<siteBase>slides/lectureN/` (derived from astro.config.mjs) + hash router.
  - No `--download` (requires Playwright, not installed). Astro telemetry disabled during build.
- **Deploy**: GitHub Pages via `.github/workflows/deploy.yml` (added 2026-09-11). On push
  to `main` (or `workflow_dispatch`): `npm ci` in `website/`+`slides/` → root `npm run
  build` → `touch site/.nojekyll` → `upload-pages-artifact` (path `site/`) →
  `deploy-pages`. Repo Pages source must be **GitHub Actions** (Settings → Pages).
  `astro.config.mjs` `site`/`base` already point at `https://jame-louis.github.io/course-template/`.
  `netlify.toml` remains for optional Netlify fallback.

## Constraints

- No client-side JS in the website (CSS-only motion, respects prefers-reduced-motion).
- No root npm dependencies (Node built-ins only for scripts).
- Local preview: `npm run dev`/`serve` (`scripts/serve.mjs`) serves built `site/` under the
  site base with SPA fallback.
- `site/`, `website/dist/`, `website/.astro/`, `slides/dist/`, `node_modules/` are
  gitignored build artifacts.

## Open questions / trade-offs

- Incremental slide check only tracks the deck's own `.md`; shared includes
  (`pages/`, `snippets/`, `components/`, theme) need `--force` after changes.
- A root `.gitignore` exists now; no automated sync between `src/` and `website/src/content/`.

## Hydro OJ problem sets (`hydro/`)

Recurring deliverable: the instructor turns each homework into Hydro judge problems in `hydro/hwNN/`
(one self-contained package per problem, PIDs increment per lecture). Cross-cutting constraints:

- **Beginner Python, not C++.** The `/hydro-problem` skill's templates are C++-oriented and assume
  loops/branches; adapt them. Standard solution file is `std/std.py.py3` (Hydro Python3 language key).
- **Match what students know.** At hw04 the class has **not** learned `if`/`for`/`while`, so every
  problem must be solvable with **no loops and no branches** — only built-ins (`sorted`, `min`, `max`,
  `sum`, `len`, `list.index`, slicing) and one-shot `input().split()+map()` line reading.
- **Set shape** (user-chosen): 5 problems per homework = 3 基础 (may be no-input, fixed output;
  `.in` holds a `no-input` marker, small case count) + 2 综合/选做 (with input).
- **Input problems grade by strict byte-exact match** (classic traditional judge, no SPJ): the prompt
  string is fixed in the statement and the `std` emits the same prompt (then a `print()` blank line,
  then results); students must reproduce it 逐字 (含全角冒号).
- Sample test case is always `1.in/1.out` and must match `problem_zh.md`. Validate with
  `python3 hydro/hw04/validate.py` (reads case counts from each `config.yaml`).
