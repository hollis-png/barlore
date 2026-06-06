# Barlore Content Workflow

How to add new knowledge to Barlore with minimum overhead and maximum consistency.
Every entry type follows the same three-phase loop: **Source → Write → Validate**.

---

## The Core Rule

> **Sources first, writing second.**

Never start writing an entry without knowing what you will cite. A field with no source
stays empty. An empty field is honest; a fabricated number is corrupting.

---

## Phase 1: Source Intake

Before writing a single word of content, record your sources.

### Where to find sources by entry type

| Entry type | Primary source locations | Minimum credibility |
|------------|--------------------------|---------------------|
| `core/` principles | Israetel / Schoenfeld / NSCA position statements / peer-reviewed journals | `expert_consensus` |
| `exercises/` — EMG fields | PubMed (search: `[exercise name] EMG electromyography`) | `rct` |
| `exercises/` — technique fields | NSCA textbooks, reputable coaches' published work | `practitioner` |
| `exercises/` — ROM fields | Biomechanics textbooks, PubMed | `expert_consensus` |
| `programs/` | The program creator's own book or published protocol | `practitioner` |
| `crosscutting/nutrition/` | PubMed meta-analyses, Examine.com as a pointer (not as a source) | `meta_analysis` |
| `crosscutting/recovery/` | PubMed, NSCA, sports medicine journals | `expert_consensus` |

### Source intake template

For each entry you plan to write, create `raw/{category}/{id}.md` with this format:

```markdown
# Source notes: {entry id}

## Target entry
- File: {exercises|core|programs|crosscutting}/{path}.md
- Fields to fill: {list the specific YAML fields you have sources for}

## Sources

### Source 1
- Title: 
- Author(s): 
- Year: 
- URL / DOI: 
- Credibility: {meta_analysis | rct | expert_consensus | practitioner | anecdotal}
- Key facts extracted:
  - 
  - 

### Source 2
...

## What this does NOT cover
{List fields you could not find sources for — these stay empty in the entry}
```

**You do not need to fill `raw/` for every entry.** Use it when:
- The entry is complex (multiple fields, multiple sources)
- You want a record for future revisions
- You are unsure about the credibility tier

For simple entries (1 source, 1–2 facts), write directly from the source.

---

## Phase 2: Writing the Entry

Use the schema in `SCHEMA.md` for the correct fields.
Use the existing `core/sra_curve.md` or `exercises/back_squat.md` as format references.

### Writing rules by entry type

**`core/` principles**
- One concept per file. Do not combine two principles into one entry.
- Body structure: Core Definition → Mechanism / How It Works → How Systems Differ
- Keep it system-agnostic. If a system applies the principle differently, that goes in
  the system's `index.md`, not here.
- `related:` field must only reference other existing `core/` ids.

**`exercises/`**
- Frontmatter first: fill every field you have a source for. Leave the rest absent.
- Body structure: Classification → Muscles → Execution → EMG Notes (if available) →
  Common Faults → Variations/Progressions
- Each heading should include the exercise name (chunk-friendliness):
  e.g. `## Back Squat — Common Faults` not `## Common Faults`
- Add a `summary:` field — one sentence + key numbers — for chunk retrieval:
  ```yaml
  summary: >
    Barbell squat with low bar position on rear delts. Primary movers: quadriceps,
    gluteus maximus. EMG peak: vastus medialis 61% MVC at 100% 1RM (Yavuz 2015).
  ```
- `status: stub` → `partial` (some data) → `complete` (all key fields filled with sources)

**`programs/`**
- `exercises[]` is required. Every exercise listed must have `ref`, `role`, and
  `technical_notes`.
- `technical_notes` is written in second person, as a coach instructing the athlete.
  Be specific: bar position, stance width, depth cue, grip, breathing pattern.
- Week objects use `pct_tm` (percentage of training max), `pct_1rm`, or `rpe` for intensity.
- Body prose: explain *why* the program is structured the way it is, not just *what* to do.

**`crosscutting/`**
- Every claim must have a source. No general health advice without a citation.
- Section `## How Systems Differ` explains variation across systems — this is the only
  place where system-specific content appears in a crosscutting file.

---

## Phase 3: Validate

After writing, always run:

```bash
python3 scripts/build_index.py
```

Must exit 0. If it fails, the error message tells you exactly which reference is broken.

Then check if your entry moved the needle:

```bash
python3 scripts/coverage.py --todo
```

If the entry appears in the TODO list as resolved, you are done.
If it opens new gaps (e.g. you added an exercise but did not reference it from any program),
note it for next time.

Commit with a descriptive message:

```
git add {files}
git commit -m "Add {entry id}: {one-line summary of what was added}

Source: {author, title, year}
Credibility: {tier}
Fields added: {list of YAML fields filled}"
```

---

## Workflow for AI-Assisted Entries

When working with an AI agent (this is the primary authoring mode for Barlore):

1. **You identify** what needs to be written (use `coverage.py --todo`)
2. **AI searches** for the right sources (using web search tools)
3. **AI extracts** key facts and assigns credibility tier
4. **AI writes** the entry using SCHEMA.md
5. **AI runs** `build_index.py` to validate
6. **You review** the output — check that the `technical_notes` are accurate,
   the credibility tier is not inflated, and no numbers were invented
7. **Git commit**

**Your review focus**: You know the domain. The AI knows the format. Catch:
- Incorrect technique cues (the AI may hallucinate specifics)
- Inflated credibility tiers (practitioner knowledge cited as rct)
- Missing nuance (an EMG study done at one load does not generalize to all loads)

---

## Priority Order for Adding Content

Run `coverage.py --todo` to get the current list. The general priority logic:

```
1. Complete exercises that are already in programs (fill their EMG/ROM gaps first)
2. New programs (each program adds multiple exercise references at once)
3. Core principles (referenced by programs and systems)
4. Crosscutting entries (nutrition, recovery)
5. Stub exercises (promote stubs to partial/complete by movement pattern:
   squat → hinge → vertical_pull → horizontal_press → vertical_press → carry → isolation)
```

Never fill stubs in alphabetical order — prioritize by movement pattern importance
and by whether the exercise is likely to appear in the next program you plan to write.

---

## Quick Reference: Credibility Tier Assignment

| What you have | Tier |
|---------------|------|
| Systematic review / meta-analysis of multiple RCTs | `meta_analysis` |
| Single randomized controlled trial with control group | `rct` |
| Position statement from NSCA / ACSM / peer-reviewed textbook | `expert_consensus` |
| Published book / protocol by the program creator or recognized coach | `practitioner` |
| Forum posts, YouTube, personal experience | `anecdotal` |

When in doubt, assign the **lower** tier. Inflating credibility is the worst error.

---

## Files That Define the Standard

| File | Purpose |
|------|---------|
| `SCHEMA.md` | Canonical field spec — update this first when adding fields |
| `AGENTS.md` | AI agent rules — the above in condensed form |
| `glossary.md` | Canonical term names — check before naming a new entry |
| `core/muscles.yaml` | All valid muscle ids — check before adding muscle references |
| `exercises/back_squat.md` | Reference for a complete exercise entry |
| `programs/powerlifting/5_3_1.md` | Reference for a complete program entry |
