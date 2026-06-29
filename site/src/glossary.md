---
id: glossary
name: Glossary
category: meta
---

# Glossary

Canonical term reference for the Barlore knowledge base. If you're new to training and see an unfamiliar term in a program or exercise page, look it up here.

## Reading a Program Table

Most programs present exercises in a table like this:

| Exercise | Sets × Reps | Intensity | Notes |
|----------|-------------|-----------|-------|
| Back Squat | 3 × 5 | 80% TM | Primary compound |
| Bench Press | 4 × 8–12 | RPE 8 | Double progression |
| Side Lateral Raise | 3 × 15–20 | — | Isolation accessory |

Here's what each column means:

- **Sets × Reps** — `3 × 5` means 3 sets of 5 repetitions each. `4 × 8–12` means 4 sets of 8 to 12 reps (use double progression: add reps each session until you hit the top of the range, then add weight).
- **Intensity** — How heavy to go. Can be expressed as `% TM` (percentage of training max), `% 1RM` (percentage of one-rep max), or `RPE` (rate of perceived exertion). See sections below.
- **AMRAP** — "As Many Reps As Possible." Written as `5+` — do at least 5, then keep going until you can't complete another rep with good form.
- **Rest** — Time between sets. If not specified, use 2–3 minutes for compound lifts and 1–2 minutes for isolation exercises.

### Double Progression

The most common beginner progression method. Two variables increase in sequence:

1. **Add reps** at the same weight until you reach the top of the prescribed range on all sets
2. **Add weight** and reset to the bottom of the range

Example: Bench Press is prescribed at `3 × 8–12`.
- Session 1: 60 kg × 8, 8, 8 → not at top of range yet, stay at 60 kg
- Session 4: 60 kg × 10, 11, 12 → hit 12 on all sets → next session: 62.5 kg × 8, 8, 8

---

## Movement Patterns

| Term | Aliases | Description |
|------|---------|-------------|
| Squat | back squat, front squat | Knee-dominant movement — you bend at the knees and hips to lower your body, then stand up |
| Hinge | hip hinge, deadlift pattern | Hip-dominant movement — you push your hips back while keeping your legs relatively straight |
| Horizontal press | bench, push | Pressing a weight away from your chest (lying down or standing) |
| Vertical press | overhead press, OHP | Pressing a weight overhead |
| Horizontal pull | row | Pulling a weight toward your torso |
| Vertical pull | pull-up, pulldown | Pulling your body up or pulling a weight down from above |
| Carry | loaded carry, farmer's walk | Walking while holding heavy weight |
| Isolation | single-joint | Movement that works one muscle group through one joint (curls, raises, extensions) |

---

## Intensity & Effort

| Term | What it means | Example |
|------|---------------|---------|
| 1RM | One-rep max — the heaviest weight you can lift once | "My squat 1RM is 140 kg" |
| e1RM | Estimated 1RM — calculated from a lighter set using a formula | See `testing_protocols` |
| TM | Training max — 85–90% of your 1RM, used to calculate working weights | "TM = 126 kg (90% of 140 kg)" |
| % TM | Percentage of training max | "65% TM" = 65% × 126 = 82 kg |
| % 1RM | Percentage of true one-rep max | "80% 1RM" = 80% × 140 = 112 kg |
| RPE | Rate of perceived exertion (1–10 scale) | RPE 8 = you could have done 2 more reps |
| RIR | Reps in reserve — how many reps you had left | RIR 2 = you stopped with 2 reps left in the tank |

### RPE / RIR Quick Reference

| RPE | RIR | What it feels like |
|-----|-----|-------------------|
| 10 | 0 | Maximum effort — could not have done another rep |
| 9 | 1 | Very hard — maybe one more rep possible |
| 8 | 2 | Hard — two more reps possible |
| 7 | 3 | Moderate — three more reps possible, starting to feel challenging |
| 6 | 4 | Moderate — four more reps, a good warm-up set weight |

---

## Program Structure Terms

| Term | Meaning |
|------|---------|
| Compound exercise | A movement that uses multiple joints and muscle groups (squat, deadlift, bench press, row) |
| Isolation exercise | A movement that targets one muscle group through one joint (curl, lateral raise, leg extension) |
| Primary / main lift | The most important exercise in a session — usually a heavy compound movement |
| Supplemental / secondary | A supporting exercise that builds the same muscles as the primary, often at lighter weight or different angle |
| Accessory | A smaller exercise that targets a specific weak point or muscle group (usually isolation) |
| Superset | Two exercises performed back-to-back without rest between them |
| Drop set | After reaching failure, immediately reduce the weight and continue repping |
| Rest-pause | After reaching failure, rest 10–15 seconds, then do a few more reps at the same weight |
| Working sets | The sets that count — not warm-up sets |
| Warm-up sets | Lighter sets before working weight to prepare your muscles and joints |
| Deload | A planned easy week (reduced weight or volume) to let your body recover. See `deload` |
| Mesocycle | A training block, usually 4–6 weeks, with a specific focus |
| Microcycle | One week of training |

---

## Periodization Terms

| Term | Meaning |
|------|---------|
| Linear periodization | Gradually increase weight and decrease reps over weeks |
| Undulating periodization | Vary intensity and volume within each week (e.g., heavy Monday, light Wednesday, moderate Friday) |
| Block periodization | Dedicate each mesocycle to one quality (e.g., 4 weeks hypertrophy, 4 weeks strength, 2 weeks peaking) |
| Conjugate | Train multiple qualities simultaneously with rotating exercise variations (Westside method) |

---

## Exercise Role in Programs

| Term | In program files | Meaning |
|------|-----------------|---------|
| Primary | `role: primary` | The main lift — heaviest, done first, defines the session |
| Supplemental | `role: supplemental` | Supports the primary — similar pattern, moderate load |
| Accessory | `role: accessory` | Targets a specific muscle — lighter load, higher reps |

---

## Credibility Tiers

Used in source citations. From strongest to weakest evidence:

| Tier | What it is | Example |
|------|-----------|---------|
| `meta_analysis` | Statistical combination of multiple studies | "Schoenfeld 2017 meta-analysis of 15 RCTs" |
| `rct` | Randomized controlled trial — gold standard single study | "Longland 2016 — 40 trained men, 4 weeks" |
| `expert_consensus` | Position statement from professional body | "NSCA Essentials of Strength Training" |
| `practitioner` | Published work from experienced coach | "Wendler's 5/3/1 book" |
| `anecdotal` | Gym tradition, forums, personal experience | "Most lifters find that..." |

---

## Muscle Roles

| Term | In exercise files | Meaning |
|------|------------------|---------|
| Primary | `role: primary` | The main muscle producing force — this is the muscle the exercise "trains" |
| Secondary | `role: secondary` | Helps the primary but is not the main target |
| Stabilizer | `role: stabilizer` | Holds a joint in position but doesn't produce movement |

---

## Nutrition Terms

| Term | Meaning |
|------|---------|
| TDEE | Total Daily Energy Expenditure — how many calories you burn per day |
| Surplus | Eating more calories than your TDEE — for muscle gain |
| Deficit | Eating fewer calories than your TDEE — for fat loss |
| Maintenance | Eating at your TDEE — body weight stays stable |
| MPS | Muscle Protein Synthesis — the process of building new muscle tissue |
| Leucine threshold | The minimum leucine per meal (~2–3 g) to trigger MPS |
| Recomp | Body recomposition — gaining muscle and losing fat simultaneously. See `body_recomposition` |

---

## Abbreviations

| Abbreviation | Full term |
|-------------|-----------|
| BB | Barbell |
| DB | Dumbbell |
| KB | Kettlebell |
| BW | Bodyweight |
| OHP | Overhead Press |
| RDL | Romanian Deadlift |
| GHR | Glute Ham Raise |
| PPL | Push Pull Legs (program split) |
| UL | Upper/Lower (program split) |
| BBB | Boring But Big (5/3/1 variation) |
| AMRAP | As Many Reps As Possible |
| EMOM | Every Minute On the Minute |
| WOD | Workout of the Day (CrossFit) |
| DOMS | Delayed Onset Muscle Soreness |
| SRA | Stimulus-Recovery-Adaptation |
| MEV | Minimum Effective Volume |
| MAV | Maximum Adaptive Volume |
| MRV | Maximum Recoverable Volume |
| BFR | Blood Flow Restriction |
