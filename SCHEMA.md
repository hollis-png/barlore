# Entry Schema

Formal field specification for every entry `category`. `build_index.py --check`
validates entries against this spec. When you add a field, update this file
*and* the validator in the same change.

> **Architecture note:** Programs are top-level (`programs/{system}/`). The former
> `systems/*/lenses/` layer has been removed. Exercise-specific training knowledge
> (technique, intensity, weekly prescription) now lives inside each program entry
> under the `exercises[]` field.

Conventions:
- **req** = required, **opt** = optional
- List fields are YAML lists even when they hold one item: `pattern: [squat]`
- All `*_ref` / relation fields hold entry `id`s, never file paths or display names
- Names in relation fields must resolve to a real entry, or `--check` fails

---

## category: principle  (`core/`)

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `id` | req | str | snake_case, unique, matches filename |
| `name` | req | str | Canonical name (see `glossary.md`) |
| `aliases` | opt | list[str] | Other names |
| `category` | req | const | Always `principle` |
| `applies_to` | req | list[str] | System ids, or `[all_systems]` |
| `related` | opt | list[id] | Other principle ids; must resolve |
| `sources` | opt | list[source] | See Source object below |

---

## category: exercise  (`exercises/`)

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `id` | req | str | snake_case, unique, matches filename |
| `name` | req | str | Canonical name |
| `aliases` | opt | list[str] | Other names |
| `category` | req | const | Always `exercise` |
| `pattern` | req | list[enum] | From glossary patterns; a movement may list several |
| `equipment` | req | list[str] | |
| `difficulty` | opt | object | See Difficulty object below — only fill if justified |
| `muscles` | opt | list[muscle] | See Muscle object below — only fill fields with a source |
| `muscle_activation_studies` | opt | list[study] | See EMG Study object below |
| `joint_rom_required` | opt | object | See ROM object below |
| `strength_curve` | opt | object | See Strength Curve object below |
| `injury_risk` | opt | object | See Injury Risk object below |
| `variations` | opt | list[id] | Same pattern, altered execution; must resolve |
| `progressions` | opt | list[id] | Easier regressions of this movement; must resolve |
| `alternatives` | opt | list[id] | Different movement, similar training purpose; must resolve |
| `sources` | opt | list[source] | |

**Policy: only fill quantitative fields when a source is available.** An absent
field is honest; an unsourced number looks like a fact.

Relation semantics (keep these distinct):
- `variations` — the *same* lift done differently (front squat ↔ back squat)
- `progressions` — a *simpler* path toward this lift (box squat → back squat)
- `alternatives` — a *different* lift serving the same role (leg press for back squat)

Relations are declared one-directionally and the validator reports asymmetries
as warnings. Do not hand-write both sides.

---

### Difficulty object

```yaml
difficulty:
  technical_complexity: 3     # 1–5; learning curve for correct technique
  strength_prerequisite: 3    # 1–5; base strength needed to train safely
  mobility_prerequisite: 3    # 1–5; joint range of motion demands
```

Ratings are 1 (minimal) to 5 (very high). Each dimension is independent;
a movement can be technically simple but have high mobility demands.

---

### Muscle object

```yaml
muscles:
  - id: vastus_lateralis       # canonical id from core/muscles.yaml
    role: primary              # primary | secondary | stabilizer
    # Do NOT add an 'emphasis' rating without an EMG source — use the
    # muscle_activation_studies field for quantified data instead.
```

`role` values:
- `primary` — prime mover; produces the majority of the joint moment
- `secondary` — synergist; contributes but is not the main driver
- `stabilizer` — isometric; maintains joint position under load

---

### EMG Study object

```yaml
muscle_activation_studies:
  - source_id: yavuz_2015        # short key matching a sources[] entry
    doi: "10.1080/..."
    n: 14                        # sample size
    population: "trained males"
    condition:
      load_pct_1rm: 80           # % of 1RM used
      bar_position: high_bar     # high_bar | low_bar
      depth: parallel            # parallel | below_parallel | quarter
      phase: concentric          # concentric | eccentric | full_rep
    measurements:
      - muscle: vastus_lateralis
        mean_pct_mvc: 45.9
        sd: 13.9
      - muscle: gluteus_maximus
        mean_pct_mvc: 28.8
        sd: 18.9
```

Multiple studies at different conditions (loads, depths, bar positions) can
be listed. Never aggregate across studies — list each as a separate object.

---

### ROM object

```yaml
joint_rom_required:
  ankle_dorsiflexion_deg: 20    # minimum for parallel depth, flat foot
  hip_flexion_deg: 120
  thoracic_extension_deg: 15   # for maintaining upright torso
  source: "NASM / Greene 1994"
```

---

### Strength Curve object

```yaml
strength_curve:
  type: ascending               # ascending | descending | bell_shaped
  sticking_point: bottom_third  # where in the ROM the lift is hardest
  peak_force_position: lockout  # where the lift is easiest
  notes: "Hip moment arm peaks at sticking point"
  source: "van den Tillaar & Andersen 2021"
```

---

### Injury Risk object

```yaml
injury_risk:
  joint_stress:
    knee: moderate              # low | moderate | high
    lower_back: moderate
    shoulder: low
  common_injuries:
    - structure: patellar_tendon
      mechanism: overuse
      risk_factors: [high_volume, rapid_load_increase]
  contraindications:
    - acute_knee_injury
    - lumbar_herniation
```

Risk levels are qualitative labels, not invented numbers. Only list
`common_injuries` entries with a plausible mechanism; do not invent incidence
percentages without an epidemiological source.

---

## category: program  (`programs/{system}/`)

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `id` | req | str | snake_case, unique |
| `name` | req | str | |
| `aliases` | opt | list[str] | |
| `category` | req | const | Always `program` |
| `system` | req | str | Must match a system folder name |
| `goal` | req | str | One line: what the program develops |
| `level` | req | enum | `beginner` \| `intermediate` \| `advanced` |
| `duration_weeks` | opt | int | Length of one cycle |
| `frequency_per_week` | opt | int | Training days per week |
| `periodization` | opt | enum | `linear` \| `undulating` \| `block` \| `conjugate` |
| `progression_model` | req | str | How load/volume advances |
| `exercises` | req | list[program_exercise] | See Program Exercise object below |
| `sources` | opt | list[source] | |

Body of a program entry should hold the actual weekly structure (a table is fine),
the progression rule in prose, and when to deload or reset.

---

### Program Exercise object

Each entry in `exercises[]` describes how the program uses one specific movement:

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `ref` | req | id | Must resolve to an exercise in `exercises/` |
| `role` | req | enum | `primary` \| `supplemental` \| `accessory` |
| `frequency_per_week` | opt | int | How many times per week this lift is trained |
| `technical_notes` | req | str | This program's technique prescription for this movement. Write in second person, as a coach giving instructions. Be specific: bar position, stance, depth cues, grip, breathing. |
| `weeks` | opt | list[week] | Per-week prescriptions |

---

### Week object

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `week` | req | int | Week number |
| `label` | opt | str | e.g. `deload` |
| `sets` | req | int | Number of working sets |
| `reps` | req | list | Can be int or string (e.g. `"5+"` for AMRAP) |
| `intensity` | req | list[intensity_unit] | See Intensity unit object |

---

### Intensity unit object

```yaml
intensity:
  - {pct_tm: 65}                    # percentage of training max
  - {pct_1rm: 80}                   # percentage of true 1RM
  - {rpe: 8}                        # RPE target
  - {pct_tm: 85, amrap: true}       # AMRAP set
```

---

## category: nutrition  (`crosscutting/nutrition/`)
## category: recovery  (`crosscutting/recovery/`)

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `id` | req | str | snake_case, unique |
| `name` | req | str | |
| `aliases` | opt | list[str] | |
| `category` | req | const | `nutrition` or `recovery` |
| `applies_to` | req | list[str] | System ids, or `[all_systems]` |
| `related` | opt | list[id] | Other crosscutting ids; must resolve |
| `sources` | opt | list[source] | |

---

## category: system_overview  (`systems/*/index.md`)

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `id` | req | str | unique |
| `name` | req | str | System display name |
| `category` | req | const | Always `system_overview` |
| `goal` | req | str | One line |

---

## Source object

Used inside any `sources` list:

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `title` | req | str | |
| `author` | opt | str | |
| `credibility` | req | enum | `meta_analysis` \| `rct` \| `expert_consensus` \| `practitioner` \| `anecdotal` |

Tiers, strongest to weakest evidence: `meta_analysis` > `rct` >
`expert_consensus` > `practitioner` > `anecdotal`.
