# AGENTS.md

Operational guide for AI agents working in the Barlore repository.
Read this before touching any file.

---

## What This Project Is

**Barlore** is a structured, evidence-tiered knowledge base for strength and physique training.
It is a *compiled wiki*, not a database — every entry is human-reviewed Markdown with YAML
frontmatter. Credibility and referential integrity are the two non-negotiable properties.

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
core/          Training science principles (progressive_overload, periodization, sra_curve)
crosscutting/  Nutrition and recovery (applies to all systems)
system_guides/ Programming logic per system × level — sits between systems/ and programs/
index/         AUTO-GENERATED — never hand-edit
scripts/       Build and validation tools
mcp-server/    MCP server (TypeScript) — stdio + Cloudflare Workers
site/          Static website (VitePress + GitHub Pages)
prompts/       AI prompt templates (plan generator)
```

---

## Layer Rules

### exercises/
- Every entry describes **what the movement is** — anatomy, mechanics, execution, EMG data.
- **Never add system-specific technique, intensity tables, or program recommendations here.**
- Quantitative fields (`muscles`, `muscle_activation_studies`, `joint_rom_required`,
  `strength_curve`) must have a cited source. Absent field = honest; unsourced number = lie.
- `status` field: `stub` (imported, unreviewed) → `partial` (some data) → `complete` (reviewed).
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

### system_guides/

- Each file covers **one system × one level** (e.g., `strongman_intermediate_guide.md`)
- Answers: *how* to program this system at this level — weekly structure logic, structural constraints, load decision framework, milestones, and common violations
- **Not** a named program — no specific exercise prescriptions or concrete rep/set week tables (those live in `programs/`)
- **Not** a system overview — athlete profile, philosophy, and distinguishing principles stay in `systems/index.md`
- Schema uses `type: system_guide` (not `category`), plus `system`, `level`, `frequency_per_week_range`, `periodization_style`
- File naming: `{system}_{level}_guide.md`; `level` is `intermediate` or `advanced`
- Beginner-level guides are intentionally absent — the Progression Pathway section in `systems/index.md` is sufficient at that level
- **Current coverage**: all 6 systems × intermediate + advanced = 12 guides.

### core/ and crosscutting/
- Principle entries define the concept only. How each system applies it lives in `systems/`.
- `applies_to: [all_systems]` is the default.

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
cd encyclopedia          # repo root
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

---

## File Naming

- All ids: `snake_case`, unique across their category, matches filename without extension
- Exercise files: `exercises/{id}.md`
- Program files: `programs/{system}/{id}.md`
- System files: `systems/{system}/index.md`
- New systems require a corresponding folder in `programs/`

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
- **Index pages** (`site/src/exercises/index.md`, etc.) are version-controlled; copied content files are not
