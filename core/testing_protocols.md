---
id: testing_protocols
name: Testing Protocols
aliases: [1RM test, one rep max, rep max testing, training max, TM, estimated 1RM, strength testing, max testing]
category: principle
applies_to: [all_systems]
related: [progressive_overload, rpe_rir, periodization, deload]
sources:
  - title: "Essentials of Strength Training and Conditioning (4th Edition)"
    author: "Haff, G. G., Triplett, N. T. (Eds.), National Strength and Conditioning Association"
    year: 2016
    publisher: "Human Kinetics"
    credibility: expert_consensus
  - title: "Validity of predictive equations for estimating 1RM in trained and untrained subjects"
    author: "LeSuer, D. A., McCormick, J. H., Mayhew, J. L., Wasserstein, R. L., Arnold, M. D."
    year: 1997
    journal: "Journal of Strength and Conditioning Research"
    volume: 11
    issue: 4
    pages: "211-213"
    credibility: rct
  - title: "5/3/1: The Simplest and Most Effective Training System for Raw Strength"
    author: "Wendler, Jim"
    year: 2011
    publisher: "Jim Wendler LLC"
    credibility: practitioner
  - title: "Prediction of one repetition maximum strength from multiple repetition maximum testing and anthropometry"
    author: "Brzycki, Matt"
    year: 1993
    journal: "Journal of Strength and Conditioning Research"
    volume: 7
    issue: 1
    pages: "39-42"
    credibility: practitioner
  - title: "Autoregulatory Progressive Resistance Exercise: A review"
    author: "Mann, J. B., Thyfault, J. P., Ivey, P. A., Sayers, S. P."
    year: 2010
    journal: "Journal of Strength and Conditioning Research"
    volume: 24
    issue: 6
    pages: "1588-1596"
    doi: "10.1519/JSC.0b013e3181afe658"
    credibility: expert_consensus
---

# Testing Protocols

Most training programs prescribe intensity as a percentage of a reference number — either a true 1RM (one-repetition maximum) or a training max. Knowing how to establish, estimate, and re-test these numbers is a prerequisite for following any percentage-based program. This entry covers when and how to test, how to estimate without testing, and how to set a training max.

---

## True 1RM Testing

A true 1RM test determines the maximum weight you can lift for a single repetition with correct technique. It is the most accurate way to calibrate program intensities, but it carries trade-offs: it requires experience with heavy singles, generates significant fatigue, and carries elevated injury risk for beginners.

### When to Test

- **Before starting a percentage-based program** that uses `pct_1rm` intensity (e.g., Texas Method, Catalyst 12-Week).
- **At the end of a training block** to measure progress — typically after a deload week, when fatigue is cleared.
- **In competition** (powerlifting, Olympic weightlifting, strongman).

### When Not to Test

- **Beginners (< 6 months training)**: Technique under maximal load is unreliable. Use estimated 1RM or training max instead.
- **Mid-block**: Testing during an accumulation phase wastes a session and produces artificially low numbers due to accumulated fatigue.
- **Frequent retesting**: 1RM testing more often than every 8–12 weeks is unnecessary. Strength changes slowly enough that monthly testing produces noise, not signal.

### Protocol (NSCA Standard)

The NSCA protocol (Haff & Triplett, 2016) is the gold standard for 1RM testing:

1. **General warm-up**: 5–10 min light cardio.
2. **Specific warm-up ramp**:
   - 50% estimated 1RM × 8 reps
   - 70% × 5 reps
   - 80% × 3 reps
   - 90% × 1 rep
3. **Testing attempts**:
   - Attempt 1: 95% estimated 1RM (should feel heavy but confident)
   - Attempt 2: +2.5–5 kg if Attempt 1 succeeded; repeat previous weight if failed
   - Attempt 3: +2.5 kg if Attempt 2 succeeded; stop if failed
   - Maximum 3–5 attempts. Rest 3–5 minutes between attempts.
4. **Record the highest successful single** as the 1RM.

**Critical rules**:
- The rep must meet the movement standard: full depth on squats, pause on bench (if testing for powerlifting), full lockout on deadlifts.
- If form breaks down significantly, the attempt does not count even if completed.
- Always use a spotter for squat and bench press; use safety bars or pins if training alone.

---

## Estimated 1RM (Rep-Max Formulas)

When a true 1RM test is impractical, you can estimate it from a submaximal set. Several formulas exist; the two most widely used:

### Epley Formula

```
Estimated 1RM = weight × (1 + reps / 30)
```

### Brzycki Formula

```
Estimated 1RM = weight × (36 / (37 − reps))
```

Both formulas are most accurate in the 3–10 rep range (LeSuer et al. 1997). Above 10 reps, they increasingly overestimate; below 3, they approach the true 1RM anyway.

### Example

You bench press 80 kg for 6 reps:
- Epley: 80 × (1 + 6/30) = 80 × 1.2 = **96 kg**
- Brzycki: 80 × (36 / 31) = 80 × 1.161 = **93 kg**

The true value is likely between the two estimates. For programming purposes, use the **lower estimate** — an underestimated 1RM produces slightly lighter working weights, which is safer than the reverse.

### When to Use Estimates

- **Beginners**: Always. Run a "top set" at RPE 8–9 for 3–5 reps and plug into the formula.
- **Program start**: Many programs don't require a true 1RM — an estimate from a 3–5RM test is sufficient.
- **Progress tracking**: Re-estimate every 4–6 weeks using a heavy set within normal training. No separate test session needed.

---

## Training Max (TM)

The training max is a deliberately conservative number used to calculate working weights. It ensures that prescribed percentages remain submaximal even on bad days, preserving technique quality and sustainable progression.

### What It Is

A training max is typically set at **85–90% of the true or estimated 1RM**. Wendler (2011) popularized this concept in the 5/3/1 program, recommending 90% for experienced lifters and 85% for beginners or when starting a new cycle.

```
Training Max = Estimated 1RM × 0.85 (conservative) or × 0.90 (standard)
```

### Why It Exists

- **Accounts for daily variation**: Strength fluctuates ±5% based on sleep, stress, nutrition, and accumulated fatigue. A TM at 90% ensures that even a "bad day" 1RM is above the TM.
- **Preserves rep quality**: Working sets calculated from a TM are executable with good form for the prescribed reps. Sets calculated from a true 1RM often require grinding reps that degrade technique.
- **Enables long-term progression**: Programs like 5/3/1 add 2.5–5 kg to the TM per cycle. Starting at 90% gives 6–12 months of progression before the TM approaches the true 1RM.

### Example

| True 1RM | TM (90%) | Week 1 working weight (5/3/1: 65% TM) | Effective % of true 1RM |
|----------|----------|----------------------------------------|------------------------|
| 140 kg | 126 kg | 82 kg | 59% |
| 140 kg | 119 kg (85%) | 77 kg | 55% |

The gap between TM-based percentages and true 1RM percentages is the built-in safety margin.

### Programs That Use TM

| Intensity notation | Meaning | Example programs |
|-------------------|---------|-----------------|
| `pct_tm` | Percentage of training max | 5/3/1, 5/3/1 BBB |
| `pct_1rm` | Percentage of true 1RM | Texas Method, most Olympic programs |
| `rpe` | Autoregulated, no fixed % | RP Hypertrophy, GZCLP (tier system) |

---

## Re-Testing and TM Updates

### When to Re-Test

| Scenario | Action |
|----------|--------|
| End of a 4-week 5/3/1 cycle | Add 2.5 kg (upper) or 5 kg (lower) to TM. No re-test needed. |
| End of a 12-week block | Optional 1RM test after deload week |
| Program switch | Estimate from a recent heavy set; start the new program conservatively |
| Return from injury or layoff | Re-test from scratch; do not use old numbers |
| Stall (2+ cycles without AMRAP improvement) | Reset TM to 85–90% of current estimated 1RM |

### How to Re-Test Without a Max-Out Session

Many programs build testing into normal training:

- **AMRAP sets** (5/3/1, GZCLP): The rep count on the AMRAP set provides an ongoing estimated 1RM. If your AMRAP consistently exceeds the prescribed minimum, your estimated 1RM has increased. No separate test needed.
- **RPE-based top sets**: If you hit a prescribed RPE 8 single, that single is approximately your 92% 1RM (see `rpe_rir`). Multiply by 1.08 to estimate current 1RM.
- **Rep PR tracking**: If you beat a previous rep record at the same weight, your 1RM has increased even without testing it directly.

---

## Testing for Non-Barbell Systems

### Calisthenics

There is no "1RM" for bodyweight exercises. Instead, test:
- **Max reps**: Unbroken set to failure (pull-ups, push-ups, dips)
- **Max hold time**: Handstand, L-sit, planche (seconds)
- **Progression level**: Which variation can be performed for the target rep range (e.g., tuck front lever for 10s but not advanced tuck)

Re-test every 4–6 weeks. Progress is expressed as either more reps, longer holds, or advancing to a harder variation.

### CrossFit

CrossFit uses benchmark WODs (Fran, Grace, Murph) as testing proxies. Barbell lifts are tested as true 1RMs in strength cycles. Gymnastic movements use max reps or max unbroken sets.

### Strongman

Event-specific testing: max deadlift, max log press, max distance carry at fixed weight, fastest time for a medley. These are tested in mock competitions or at the end of training blocks.

---

## Common Mistakes

1. **Testing too often**: Monthly 1RM tests are unnecessary fatigue generators. Every 8–12 weeks is sufficient.
2. **Testing when fatigued**: Always test after a deload or light week. A 1RM test during Week 4 of a volume block will underestimate your true max.
3. **Using true 1RM for programming**: Unless a program explicitly calls for `pct_1rm`, use a training max. Programming off a true 1RM produces overly heavy working sets that degrade form and limit volume.
4. **Skipping warm-up sets**: The ramp protocol is not optional. Cold muscles produce lower maxes and higher injury risk.
5. **Ego-driven attempts**: Stop at 3 attempts if progress has stalled. A 4th or 5th grinding attempt produces excessive fatigue and injury risk for diminishing information.

---

## How Systems Differ

- **Powerlifting**: The most formalized testing culture. Competition is itself a 1RM test. Training cycles peak toward a test day with planned deloads. Most programs use either `pct_1rm` or `pct_tm`.
- **Bodybuilding**: 1RM testing is uncommon. Progress is tracked through rep PRs, visual progress, and estimated 1RM from working sets. Programs use `rpe` or rep-range targets rather than percentages.
- **Olympic Weightlifting**: Regular 1RM testing on snatch and clean & jerk is standard because competition is at 1RM. Daily training often includes heavy singles as autoregulation. Training percentages are based on recent best, updated frequently.
- **Calisthenics**: No barbell 1RM. Progress is tracked through rep maxes and progression advancement. See the calisthenics section above.
- **CrossFit**: Periodic 1RM testing for benchmark lifts (back squat, deadlift, clean, snatch). WOD benchmarks serve as fitness tests.
- **Strongman**: Event-specific testing in mock competitions. Barbell lifts are tested similarly to powerlifting.
