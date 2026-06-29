# AGENTS.md

Operational guide for AI agents working in the Barlore repository.
Read this before touching any file.

---

## What This Project Is

**Barlore** is a structured, evidence-tiered knowledge base for strength and physique training.
It is a *compiled wiki*, not a database — every entry is human-reviewed Markdown with YAML
frontmatter. Credibility and referential integrity are the two non-negotiable properties.

---

## Current Coverage

| Category | Count | Notes |
|----------|-------|-------|
| Exercises | 688 total | 92 complete, 595 stubs (all have pattern + equipment) |
| Programs | 53 | Across 6 systems, beginner to advanced |
| Core principles | 11 | Including hypertrophy_mechanisms, training_to_failure, testing_protocols |
| Crosscutting | 22 | Nutrition (8), recovery (4), injury prevention (4), cardio (3), special populations (3) |
| System guides | 12 | All 6 systems × intermediate + advanced |

---

## Content Creation Process

See `WORKFLOW.md` for the full process: source intake → write → validate.
The short version: **sources first, writing second. Never invent numbers.**

---

## Architecture: Three Independent Layers

```
exercises/     Movement base entries. Neutral. No system bias.
systems/       Training system philosophy. No exercise prescriptions.
programs/      Named training programs. Exercise prescriptions live here.
```

These three layers are **peers connected by references**, not a hierarchy.
A movement is never "owned" by a system. Use `id` references across layers.

Supporting layers:
```
core/            Training science principles (11 entries)
                 progressive_overload, periodization, sra_curve, volume_landmarks,
                 rpe_rir, rep_continuum, specificity, deload,
                 hypertrophy_mechanisms, training_to_failure, testing_protocols
crosscutting/    Nutrition, recovery, injury prevention, cardio, special populations
system_guides/   Programming logic per system × level (12 guides)
index/           AUTO-GENERATED — never hand-edit
scripts/         Build and validation tools
mcp-server/      MCP server (TypeScript) — stdio + Cloudflare Workers
site/            Static website (VitePress + GitHub Pages)
prompts/         AI prompt templates (plan generator)
```

---

## Layer Rules

### exercises/
- Every entry describes **what the movement is** — anatomy, mechanics, execution, EMG data.
- **Never add system-specific technique, intensity tables, or program recommendations here.**
- Quantitative fields (`muscles`, `muscle_activation_studies`, `joint_rom_required`,
  `strength_curve`) must have a cited source. Absent field = honest; unsourced number = lie.
- `status` field: `stub` (imported, unreviewed) → `partial` (some data) → `complete` (reviewed).
- All stubs must have `pattern` and `equipment` populated (required for site browsing).
- Relation fields (`variations`, `progressions`, `alternatives`) hold `id` values only —
  never file paths or display names.

### systems/
- Each `index.md` answers: goal, defining principles, what distinguishes this system.
- **No exercise technique. No intensity tables. No weekly structure.**
- List program ids in the `programs:` frontmatter field.

### programs/
- Each entry must have an `exercises[]` list.
- Every `exercises[].ref` must resolve to a real exercise id.
- Every `exercises[].technical_notes` must be non-empty — this is where system-specific
  technique lives (bar position, stance, depth cues, grip, breathing).
- `exercises[].weeks[]` holds the weekly prescription; use `pct_tm`, `pct_1rm`, or `rpe`
  for intensity units.
- When adding a new program, also update:
  - `systems/{system}/index.md` → `programs:` list
  - `prompts/plan_generator.md` → Section C.1 Programs Table
  - `site/src/programs/index.md` → the relevant system table

### system_guides/

- Each file covers **one system × one level** (e.g., `strongman_intermediate_guide.md`)
- Answers: *how* to program this system at this level — weekly structure logic, structural constraints, load decision framework, milestones, and common violations
- **Not** a named program — no specific exercise prescriptions or concrete rep/set week tables (those live in `programs/`)
- **Not** a system overview — athlete profile, philosophy, and distinguishing principles stay in `systems/index.md`
- Schema uses `type: system_guide` (not `category`), plus `system`, `level`, `frequency_per_week_range`, `periodization_style`
- File naming: `{system}_{level}_guide.md`; `level` is `intermediate` or `advanced`
- Beginner-level guides are intentionally absent — the Progression Pathway section in `systems/index.md` plus `crosscutting/special_populations/beginner_lifters.md` cover beginner guidance
- **Current coverage**: all 6 systems × intermediate + advanced = 12 guides.

### core/
- Principle entries define the concept only. How each system applies it lives in `systems/`.
- `applies_to: [all_systems]` is the default.
- Each entry must include a `## How Systems Differ` section.
- Use `related:` to cross-reference other core and crosscutting entries.

### crosscutting/
- Shared knowledge that applies across all systems.
- Subcategories: `nutrition/`, `recovery/`, `injury_prevention/`, `cardio/`, `special_populations/`
- Every claim must have a source. No general health advice without a citation.
- Section `## How Systems Differ` explains variation across systems.
- Special populations entries (`beginner_lifters`, `female_athletes`, `masters_athletes`)
  provide population-specific adjustments to standard programming.

---

## Schema

**`SCHEMA.md` is the canonical field specification.** Update it first when adding a field,
then update the validator in `scripts/build_index.py`.

Key enums to know:
- `pattern`: squat | hinge | horizontal_press | vertical_press | horizontal_pull |
              vertical_pull | carry | isolation
- `role` (muscle): primary | secondary | stabilizer
- `role` (program exercise): primary | supplemental | accessory
- `credibility`: meta_analysis | rct | expert_consensus | practitioner | anecdotal
- `status`: stub | partial | complete
- `level`: beginner | intermediate | advanced
- `periodization`: linear | undulating | block | conjugate

---

## Build Process

After **any** structural change, run:

```bash
python3 scripts/build_index.py
```

This must exit 0. If it fails, fix the integrity errors before committing.

What the build validates:
- Every `exercises[].ref` in a program resolves to a real exercise id
- Every relation field (`variations`, `progressions`, `alternatives`) resolves
- Every muscle id in `muscles[]` and `muscle_activation_studies[]` is in `core/muscles.yaml`
- Symmetry warnings (non-blocking) for one-sided variation links

What the build produces (in `index/`):
- `exercises.json` — flat exercise index
- `programs.json` — flat program index
- `program_exercise_index.json` — reverse map: exercise_id → [program_ids]
- `muscle_index.json` — reverse map: muscle_id → [exercise_ids]
- `coverage_report.json` — three-dimensional coverage data
- `system_guides.json` — system guide index

Check coverage with:
```bash
python3 scripts/coverage.py --todo     # highest-impact gaps
python3 scripts/coverage.py --systems  # system completeness
```

---

## Credibility Policy

**Only add quantitative fields when a source is available.**

Tier order (strongest → weakest):
`meta_analysis` > `rct` > `expert_consensus` > `practitioner` > `anecdotal`

- EMG data: require at least `rct`
- ROM requirements: `expert_consensus` minimum
- Technique recommendations: `practitioner` acceptable
- Never invent percentages or activation numbers without a source

---

## What NOT to Do

- Do not hand-edit anything in `index/` — it is auto-generated
- Do not add exercise-specific technique to `exercises/*.md` frontmatter
  (that belongs in `programs/*.md` → `exercises[].technical_notes`)
- Do not add quantitative fields without citing a source in `sources[]`
- Do not use file paths in relation fields — use `id` values only
- Do not commit without running `build_index.py` and verifying exit 0
- Do not touch `scripts/import_exercises.py` or `exercises/*.md` stub content
  unless you have a real source for the data you are adding
- Do not add a program without updating the plan generator table and system index
- Do not leave `pattern` or `equipment` empty on new exercise entries

---

## File Naming

- All ids: `snake_case`, unique across their category, matches filename without extension
- Exercise files: `exercises/{id}.md`
- Program files: `programs/{system}/{id}.md`
- System files: `systems/{system}/index.md`
- Core principle files: `core/{id}.md`
- Crosscutting files: `crosscutting/{subcategory}/{id}.md`
- New systems require a corresponding folder in `programs/`

---

## Plan Generator (`prompts/plan_generator.md`)

The plan generator is an AI prompt template that users paste into any LLM to get a
personalized training plan. It contains:

- **Section B**: User profile (goal, level, history, equipment, schedule)
- **Section C**: Decision matrix (programs table, goal mapping, equipment feasibility, benchmarks)
- **Section D**: Generation rules (Step 0–7)

Key design decisions:
- All goal and level options include plain-language descriptions for beginners
- Users can write `not_sure` for goal or level; Step 0 resolves uncertainty
- Step 7 auto-appends beginner guidance when `level = beginner`
- The programs table in C.1 must stay in sync with actual program files

---

## External Access Points

Barlore is accessible via three channels:

| Channel | URL | Purpose |
|---------|-----|---------|
| MCP Server | `https://barlore-mcp.hollisyen210.workers.dev/mcp` | AI agent structured queries (7 tools) |
| Static Site | `https://hollis-png.github.io/barlore/` | Human browsing, search-engine indexable |
| llms.txt | `https://raw.githubusercontent.com/hollis-png/barlore/main/llms.txt` | LLM directory with query workflow |

### MCP Server (`mcp-server/`)

- **Local**: `npx tsx mcp-server/src/index.ts` (stdio)
- **Remote**: Cloudflare Workers at the URL above
- **Tools**: search_exercises, get_exercise, search_by_muscle, list_programs, get_program, get_training_concept, list_muscles
- **Data**: JSON indexes bundled in worker, markdown fetched from GitHub raw on demand
- **Deploy**: `cd mcp-server && npm run deploy`

### Static Site (`site/`)

- **Stack**: VitePress + GitHub Pages
- **Auto-deploy**: Push to main triggers `.github/workflows/deploy-site.yml`
- **Content**: `site/prebuild.sh` copies markdown from repo into `site/src/` before build
- **Index pages** (`site/src/exercises/index.md`, `site/src/programs/index.md`, etc.) are version-controlled; copied content files are not
- **Sidebar config**: `site/.vitepress/config.ts` — update when adding new core or crosscutting entries
- **Programs index**: includes a "New to Training? Start Here" section with beginner program recommendations
- **Homepage**: features a "New to Training?" card linking to the beginner guide
