---
id: volume_landmarks
name: Volume Landmarks
aliases: [MEV, MAV, MRV, Minimum Effective Volume, Maximum Adaptive Volume, Maximum Recoverable Volume]
category: principle
applies_to: [all_systems]
related: [progressive_overload, sra_curve, periodization, deload]
sources:
  - title: "Scientific Principles of Hypertrophy Training"
    author: "Israetel, Hoffmann, Davis"
    year: 2021
    publisher: "Renaissance Periodization"
    credibility: practitioner
  - title: "Dose-response relationship between weekly resistance training volume and increases in muscle mass: A systematic review and meta-analysis"
    author: "Schoenfeld, Ogborn, Krieger"
    year: 2017
    doi: "10.1080/02640414.2016.1210197"
    credibility: meta_analysis
  - title: "Single vs. Multiple Sets of Resistance Exercise for Muscle Hypertrophy: A Meta-Analysis"
    author: "Krieger, James W."
    year: 2010
    doi: "10.1519/JSC.0b013e3181d4d446"
    credibility: meta_analysis
  - title: "The Effect of Weekly Set Volume on Strength Gain: A Meta-Analysis"
    author: "Ralston, Kilgore, Wyatt, Baker"
    year: 2017
    doi: "10.1007/s40279-017-0762-7"
    credibility: meta_analysis
  - title: "The Effects of Volume and Frequency of Resistance Training on Morphofunctional Variables in Resistance-Trained Young Men"
    author: "Baz-Valle, Balsalobre-Fernández, Santos-Concejero"
    year: 2022
    doi: null
    credibility: meta_analysis

# Per-muscle-group volume landmark data (sets/week)
# Population: intermediate-to-advanced trainees (3-7 years structured training)
# Source: Israetel RP practitioner framework; null high = open upper bound (e.g. "20+")
muscle_volume_landmarks:
  unit: sets_per_week
  muscle_groups:
    - id: quadriceps
      MV: 6
      MEV: 8
      MAV: {low: 12, high: 18}
      MRV: {low: 20, high: null}
    - id: hamstrings
      MV: {low: 0, high: 2}
      MEV: {low: 2, high: 4}
      MAV: {low: 2, high: 8}
      MRV: {low: 8, high: 14}
    - id: gluteus_maximus
      MV: {low: 2, high: 6}
      MEV: {low: 6, high: 8}
      MAV: {low: 8, high: 24}
      MRV: {low: 24, high: 30}
    - id: latissimus_dorsi
      MV: 8
      MEV: 10
      MAV: {low: 14, high: 22}
      MRV: {low: 25, high: null}
    - id: trapezius
      MV: {low: 0, high: 4}
      MEV: {low: 0, high: 4}
      MAV: {low: 4, high: 12}
      MRV: {low: 12, high: 20}
    - id: pectoralis_major
      MV: {low: 2, high: 4}
      MEV: {low: 4, high: 6}
      MAV: {low: 6, high: 16}
      MRV: {low: 16, high: 24}
    - id: deltoid_anterior
      MV: {low: 0, high: 2}
      MEV: {low: 0, high: 2}
      MAV: {low: 4, high: 8}
      MRV: {low: 8, high: 12}
    - id: deltoid_lateral
      MV: {low: 2, high: 6}
      MEV: {low: 6, high: 8}
      MAV: {low: 8, high: 24}
      MRV: {low: 24, high: 30}
    - id: deltoid_posterior
      MV: {low: 0, high: 4}
      MEV: {low: 0, high: 4}
      MAV: {low: 4, high: 12}
      MRV: {low: 12, high: 20}
    - id: triceps_brachii
      MV: {low: 0, high: 4}
      MEV: {low: 4, high: 6}
      MAV: {low: 6, high: 16}
      MRV: {low: 16, high: 20}
    - id: biceps_brachii
      MV: {low: 6, high: 8}
      MEV: {low: 8, high: 10}
      MAV: {low: 14, high: 20}
      MRV: {low: 20, high: 26}
    - id: erector_spinae
      MV: null
      MEV: null
      MAV: null
      MRV: null
      notes: "No direct volume landmarks; loaded isometrically via compound squats/deadlifts"
    - id: gastrocnemius_soleus
      MV: {low: 2, high: 4}
      MEV: {low: 4, high: 6}
      MAV: {low: 6, high: 16}
      MRV: {low: 16, high: 24}
    - id: rectus_abdominis
      MV: 0
      MEV: 0
      MAV: {low: 16, high: 20}
      MRV: {low: 25, high: null}
---

# Volume Landmarks

Volume landmarks are a framework for quantifying the training volume — measured in weekly
sets per muscle group — at which distinct adaptations occur. They answer the question:
**how much is enough, how much is optimal, and how much is too much?**

## The Four Landmarks

**MV — Maintenance Volume**
The minimum weekly sets required to preserve existing muscle mass. No further growth
occurs at this volume, but current size is retained. Relevant during peaking phases or
competition prep, when fatigue management takes priority over adding stimulus.

**MEV — Minimum Effective Volume**
The least volume per week that produces measurable progress for a given muscle group.
Below MEV, you maintain but do not grow. MEV is the starting point for a hypertrophy
mesocycle — week one sets begin here. It is lower than most trainees assume: for some
muscle groups, 6–8 sets per week may be sufficient to initiate growth in intermediate
lifters.

**MAV — Maximum Adaptive Volume**
The volume range within which the greatest hypertrophic adaptation occurs. MAV is a range
rather than a fixed number, and it shifts upward as training age and work capacity increase.
The goal of a well-designed mesocycle is to begin near MEV and progressively increase volume
across weeks until approaching MAV — adding stimulus while fatigue is still manageable.

**MRV — Maximum Recoverable Volume**
The highest weekly volume from which the body can still recover before the next session.
Exceeding MRV produces fatigue accumulation that outpaces adaptation: performance declines,
injury risk rises, and further volume becomes counterproductive. MRV is the ceiling of a
mesocycle; when approaching it, a deload is due.

## Landmark Order

```
MV  <  MEV  <  MAV  <  MRV
```

## Why Volume Matters: The Dose-Response Evidence

A 2017 meta-analysis (Schoenfeld, Ogborn, Krieger) confirmed a dose-response relationship
between weekly training volume and hypertrophy: more sets per muscle group produce more
growth, up to a recoverable ceiling. The practical takeaway is that most trainees
underperform because they train below MEV rather than because they need more advanced
techniques.

## Volume Landmarks by Muscle Group

Values for intermediate-to-advanced trainees (3–7 years structured training). All units: sets/week.
Source: Israetel, RP practitioner framework. "+" denotes open upper bound.

| Muscle group | MV | MEV | MAV | MRV |
|---|---|---|---|---|
| quadriceps | 6 | 8 | 12–18 | 20+ |
| hamstrings | 0–2 | 2–4 | 2–8 | 8–14 |
| gluteus_maximus | 2–6 | 6–8 | 8–24 | 24–30 |
| latissimus_dorsi | 8 | 10 | 14–22 | 25+ |
| trapezius | 0–4 | 0–4 | 4–12 | 12–20 |
| pectoralis_major | 2–4 | 4–6 | 6–16 | 16–24 |
| deltoid_anterior | 0–2 | 0–2 | 4–8 | 8–12 |
| deltoid_lateral | 2–6 | 6–8 | 8–24 | 24–30 |
| deltoid_posterior | 0–4 | 0–4 | 4–12 | 12–20 |
| triceps_brachii | 0–4 | 4–6 | 6–16 | 16–20 |
| biceps_brachii | 6–8 | 8–10 | 14–20 | 20–26 |
| erector_spinae | — | — | — | — |
| gastrocnemius_soleus | 2–4 | 4–6 | 6–16 | 16–24 |
| rectus_abdominis | 0 | 0 | 16–20 | 25+ |

Notes:
- **hamstrings**: Low absolute numbers reflect high stimulus-per-set from loaded stretch in hip hinge movements; direct sets accumulate quickly.
- **gluteus_maximus**: Can be maintained at 0 direct sets if compound squatting and hinging volume is high; MAV/MRV expand greatly during specialization blocks.
- **deltoid_anterior**: Receives heavy indirect loading from all chest and overhead pressing; direct isolation rarely needed.
- **erector_spinae**: No direct volume landmarks — loaded isometrically via all compound squatting, hinging, and lunging. Direct hypertrophy targeting is not recommended on top of compound volume.
- **rectus_abdominis**: MEV = 0 because compound bracing covers maintenance; high MAV reflects the core's resistance to fatigue under direct training.

## Practical Application

A typical hypertrophy mesocycle runs 4–6 weeks:
- **Week 1**: volume at or near MEV. Sessions feel manageable.
- **Weeks 2–4**: volume increases by 1–2 sets per muscle group per week.
- **Final week**: volume approaching MRV. Sessions feel hard; fatigue accumulates.
- **Deload week**: volume drops to MV or below. Fatigue clears, fitness is expressed.

## How Systems Differ

The landmark framework applies universally, but the absolute numbers shift significantly
by goal. Powerlifting programs keep volume for non-competition movements near MEV to
preserve recovery capacity for the competition lifts. Bodybuilding programs push toward
MAV for the target muscle groups each mesocycle. Strength athletes often operate with
lower overall set counts but higher average intensity, which changes recovery demands
and therefore MRV.

## What This Framework Does Not Replace

Volume landmarks describe weekly set volume. They do not capture:
- Load intensity (percentage of 1RM or RPE)
- Proximity to failure (sets done far from failure accumulate less stimulus at the same
  set count)
- Exercise selection quality (a poorly targeted exercise contributes fewer effective sets)

See `core/rpe_rir.md` for intensity regulation and `core/sra_curve.md` for the
recovery mechanism underlying the MRV ceiling.
