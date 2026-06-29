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


---

# Learning Roadmap

This is not a course with deadlines. It's a map of what to learn, in what order, based on where you are right now.

Each layer answers one question. Read it when that question starts bothering you — not before.

---

## Layer 1: What Should I Do?

Start here if you've never followed a structured training program, or if you're coming back after a long break.

### Step 0 — Check your conditions

Before picking a program, answer three questions:

1. **What equipment do I have?**
   - Full gym (barbells, dumbbells, cables, machines) → most programs work
   - Barbell + squat rack (home gym) → powerlifting and Olympic programs
   - Dumbbells only → bodybuilding with modifications
   - Nothing → calisthenics programs
   
2. **How many days per week can I train?**
   - 3 days → full-body programs ([Starting Strength](/programs/starting_strength), [Beginner Full-Body Hypertrophy](/programs/beginner_fullbody_hypertrophy), [BWF Recommended Routine](/programs/bwf_recommended_routine))
   - 4 days → upper/lower splits ([GZCLP](/programs/gzclp), [Beginner Upper/Lower](/programs/beginner_upper_lower))
   - 5–6 days → only if you're sure you can sustain the schedule
   
3. **How long is each session?**
   - 30–45 min → keep exercise count low (5–6 per session)
   - 45–60 min → standard beginner programs fit comfortably
   - 60+ min → you have room for extra accessories

These answers directly filter your program options. The [programs page](/programs/) lets you browse by goal, and the [AI plan generator](/ai) can recommend based on all three factors.

### Step 1 — Pick your goal

What do you actually want? Be honest — there's no wrong answer.

| You want to... | Goal | Browse |
|----------------|------|--------|
| Lift heavier weights | Strength | [Get stronger →](/programs/#strength) |
| Build visible muscle | Hypertrophy | [Build muscle →](/programs/#hypertrophy) |
| Master bodyweight skills | Skill | [Learn technique →](/programs/#skill) |
| Get more athletic | Performance | [Sport performance →](/programs/#athletic) |
| Just be healthier | General | [Stay fit →](/programs/#fitness) |

Not sure? Pick **Stay fit** — those programs build a base that transfers to any specific goal later.

### Step 2 — Pick your program

From your goal and conditions, you'll have 2–4 candidate programs. Pick one. Don't overthink it — any beginner program from any system will work for 8–12 weeks. Read the [Beginner Guide](/crosscutting/beginner_lifters) for what to expect.

### Step 3 — Read your program

Your program will have tables like this:

| Exercise | Sets × Reps | Intensity |
|----------|-------------|-----------|
| Back Squat | 3 × 6–10 | RPE 8 |

If you don't know what `3 × 6–10` or `RPE 8` means, read the [Glossary](/glossary) — specifically the "Reading a Program Table" section at the top. It takes 5 minutes and makes everything else make sense.

### Step 4 — Learn your movements

Before your first session, look up each exercise in your program. Every exercise page has:
- **What muscles it works** — so you know what you should be feeling
- **Step-by-step execution** — how to do the movement correctly
- **Common faults** — the mistakes beginners make and how to fix them

Use the search bar to find any exercise, or click the exercise links in your program's page.

::: tip
Don't try to memorize every cue. Focus on 1–2 key points per exercise for your first session. Technique improves over weeks, not in one reading.
:::

### Step 5 — Start tracking

Bring a log to every session. Write down the exercise, the weight, the sets, and the reps. Without this, you can't tell if you're progressing.

Use the [Workout Log Template](https://github.com/hollis-png/barlore/blob/main/prompts/workout_log.md) — it includes a filled-in example so you know exactly what to write.

---

## Layer 2: Why Does This Work?

Read this when you start wondering — typically a few weeks in. Maybe you're curious why the program is structured the way it is, or you're struggling with nutrition, or you're sore and wondering if that's normal.

::: info When to read this
You'll know it's time when you catch yourself thinking: "Is what I'm eating even enough?", "Why am I so sore?", or "Why does this program have me doing 3 sets instead of 5?"
:::

### Training drives the stimulus

[Progressive Overload](/core/progressive_overload) — The single most important principle. Adding weight or reps over time is what forces your body to adapt. Without it, you're exercising, not training.

### Food provides the materials

[Protein Requirements](/crosscutting/protein_requirements) — How much protein you need per day (1.6–2.2 g/kg), with a worked example and sample meal plan. This is the most impactful nutrition change you can make.

[Energy Balance](/crosscutting/energy_balance) — How many calories to eat, with a step-by-step calculation example (TDEE → surplus/deficit → macros). Includes the Mifflin-St Jeor formula and a complete worked setup for a 75 kg person.

[Body Recomposition](/crosscutting/body_recomposition) — "Can I gain muscle and lose fat at the same time?" Yes, if you're a beginner. Here's how and why it works.

### Understand the growth signal

[Hypertrophy Mechanisms](/core/hypertrophy_mechanisms) — Mechanical tension is the primary driver, not soreness, not the pump. This changes how you think about which exercises matter.

[Volume Landmarks](/core/volume_landmarks) — How many sets per muscle per week is enough? Too little and you leave growth on the table. Too much and you can't recover. This entry has the numbers.

### Recovery is where growth happens

[SRA Curve](/core/sra_curve) — Why you need rest days. Training creates the stimulus; recovery is when you actually get stronger. This explains the timing.

[Deload](/core/deload) — A planned easy week every 4–6 weeks. Not laziness — it's how you prevent accumulated fatigue from suppressing your progress.

[Sleep](/crosscutting/sleep) — 7–9 hours. Non-negotiable. This entry explains why.

---

## Layer 3: What's Next?

Read this when you hit a real decision point — not before.

::: info When to read this
You'll know it's time when: the same weight won't budge for two weeks straight, a joint starts complaining, you've finished your first 12-week cycle, or you're wondering if your program is still right for you.
:::

### Measure your progress

[Testing Protocols](/core/testing_protocols) — How to test your 1RM safely, how to estimate it from submaximal sets (Epley/Brzycki formulas), and how to set a training max. Don't test too often — every 8–12 weeks is enough.

### Push harder (selectively)

[Training to Failure](/core/training_to_failure) — When failure helps (last set of isolation work) and when it hurts (heavy compounds, early sets). The RPE 8–9 sweet spot and why most sets should stop 1–2 reps short.

### Something hurts — now what?

Pain during a movement is not normal soreness. Stop the exercise and figure out what's happening before pushing through.

[Load Management](/crosscutting/load_management) — How to adjust training load when something flares up. The 10% rule, deload triggers, and when to modify vs. when to rest.

[Connective Tissue](/crosscutting/connective_tissue) — Tendons and ligaments adapt slower than muscles. This explains why, and the gelatin + Vitamin C protocol for tendon health.

[Mobility Requirements](/crosscutting/mobility_requirements) — If a movement is limited by range of motion rather than strength, the problem is mobility. This entry covers what to do.

Don't guess — if pain persists after load reduction and a deload week, see a sports physiotherapist.

### The program isn't working anymore

This usually means one of three things:

1. **Linear progression has stalled** — You can't add weight every session anymore. This is normal after 3–6 months. You need [Periodization](/core/periodization) — organizing training into phases with varying intensity and volume instead of just adding weight every time.

2. **You've outgrown your program** — A beginner program stops working when you need more volume or specificity than it provides. Look at the [System Guides](/system_guides/) for programming guidance at the intermediate level.

3. **You want to try a different system** — That's fine. The [Programs page](/programs/) lets you browse by goal, and your strength base transfers across systems.

### Fine-tune your body composition

[Body Recomposition](/crosscutting/body_recomposition) — If you've been training for 3+ months and want to optimize your physique, this entry covers when recomp stops working and when dedicated bulk/cut cycles become more effective.

---

## Use AI to Navigate

Not sure where you are on this map? The [AI plan generator](/ai) can recommend your next step based on your current program, training history, and goals. It uses Barlore's structured data — not generic advice.

For a more detailed assessment, use the full [Learning Guide prompt](https://github.com/hollis-png/barlore/blob/main/prompts/learning_guide.md): fill in your current state and paste it into any AI chatbot to get a personalized reading list.
