---
id: inverted_row
name: Inverted Row
status: complete
category: exercise
pattern: [horizontal_pull]
equipment: [barbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: trap_middle
    role: primary
  - id: deltoid_posterior
    role: primary
  - id: biceps_brachii
    role: secondary
  - id: rhomboids
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: rectus_femoris
    role: stabilizer

# ssd_2026 literature compilation. All values %MVIC.
# Stable bar and suspension (TRX) conditions both reported.
# Erector spinae values are isometric (holding plank position), not dynamic.
# Rectus femoris 2.7% confirms minimal hip flexor demand.
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: stable_bar
      grip: overhand
    measurements:
      - {muscle: latissimus_dorsi,  mean_pct_mvc: 99.3,  sd: 53.3}
      - {muscle: trap_middle,        mean_pct_mvc: 98.6,  sd: 35.6}
      - {muscle: deltoid_posterior,  mean_pct_mvc: 103.4, sd: 35.7}
      - {muscle: biceps_brachii,    mean_pct_mvc: 67.9,  sd: 20.1}
      - {muscle: erector_spinae,    mean_pct_mvc: 29.3,  sd: null, notes: "LUES isometric 29.9%, RLES isometric 28.7%; stabilizer demand only"}
      - {muscle: rectus_femoris,    mean_pct_mvc: 2.7,   sd: null, notes: "Minimal hip flexor demand confirms spinal unloading vs standing rows"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: suspension_trx
    measurements:
      - {muscle: latissimus_dorsi,  mean_pct_mvc: 101.6, sd: 46.5}
      - {muscle: trap_middle,        mean_pct_mvc: 98.4,  sd: 54.2}
      - {muscle: deltoid_posterior,  mean_pct_mvc: 103.4, sd: 35.7}
      - {muscle: biceps_brachii,    mean_pct_mvc: 67.9,  sd: 20.1}

joint_rom_required:
  shoulder_flexion_start_deg: 90
  elbow_flexion_deg: 110
  notes: >
    Body remains in a rigid supine plank with knees bent ~90°. Movement begins with
    shoulder at 90° flexion (arms straight overhead). Concentric phase drives shoulder
    through horizontal extension to ~0° as elbows flex 90–110°. Scapulae retract
    dynamically throughout the pull.
  source: "ssd_2026"

strength_curve:
  type: descending
  sticking_point: top_quarter
  peak_force_position: first_quarter
  notes: >
    Gravity acts perpendicular to the supine torso at the start, maximizing resistance
    in the first quarter. The sticking point is the terminal lockout (top quarter) —
    here elbow flexor leverage is reduced and the remaining movement requires maximal
    scapular retraction against a shortened lever arm. This contrasts with standing
    rows, which display an ascending-descending (bell-shaped) curve with peak force
    at mid-range.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
    lower_back: low
  common_injuries:
    - structure: wrist
      mechanism: hyperextension_under_load
      risk_factors: [bar_too_high, insufficient_grip_strength, fatigue]
  contraindications: []

variations: []
progressions: []
alternatives: [bent_over_barbell_row]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Inverted Row

The inverted row is a closed-chain, bodyweight horizontal pulling exercise performed beneath a fixed bar set to roughly waist height. The lifter hangs supine with arms extended, body rigid in a plank, and pulls their chest to the bar by flexing the elbows and retracting the scapulae. It elicits near-identical back and shoulder activation to standing rows while almost completely eliminating lumbar erector spinae demand — making it the primary horizontal rowing substitute for athletes with lower back pathology or for general training contexts where spinal loading must be managed.

## Execution

1. Set a bar in a rack to approximately waist height; lie beneath it with arms fully extended and hands just outside shoulder width, overhand grip
2. Extend the body into a rigid plank — hips up, heels on the floor, knees bent ~90°; do not let the hips sag
3. Pull the chest toward the bar by flexing the elbows and driving the shoulder blades together and down
4. Pause briefly when the chest touches the bar; lower under control to full arm extension
5. Difficulty is adjusted by bar height — lower bar = greater bodyweight fraction = harder

## What the EMG Data Shows

**Primary movers** (stable bar, overhand):

- Latissimus dorsi: 99.3 ± 53.3% MVIC
- Middle trapezius: 98.6 ± 35.6% MVIC
- Posterior deltoid: 103.4 ± 35.7% MVIC
- Biceps brachii: 67.9 ± 20.1% MVIC

These values are equivalent to the standing bent-over barbell row for LD and trap_middle — the inverted row is not a reduced-stimulus exercise.

**Spinal load contrast**: Erector spinae activation is 28.7–29.9% MVIC (isometric stabilizer only) and rectus femoris is 2.7% MVIC. In the standing bent-over row, the ES must eccentrically control a loaded hip hinge under high shear — here it only maintains a horizontal plank. This is the key clinical trade-off: equal back development stimulus, dramatically lower spinal cost.

**Suspension (TRX) variation**: LD increases marginally to 101.6 ± 46.5% MVIC; the primary difference is instability demand rather than a meaningful change in primary mover activation.

## The Spinal Unloading Mechanism

The inverted row achieves spinal unloading through body position, not exercise modification. In a standing bent-over row at ~75° of hip flexion, the erector spinae must counteract both the gravitational moment of the torso and the additional moment created by the loaded bar — generating compressive and shear forces at the lumbar discs that increase linearly with load. In the inverted row, the body is horizontal and the spine is not resisting a gravitational flexion moment. The ES fires isometrically only to prevent sagging. Load capacity is limited to bodyweight fraction rather than absolute load, but the neuromuscular stimulus to the target muscles (LD, middle trap, posterior delt) is preserved.

## Strength Curve

The inverted row has a steep descending curve — hardest at the bottom where gravity acts directly perpendicular to the body. This is opposite to standing rows, which build to peak resistance at mid-range. Trainees who struggle with lockout at the top can place the bar slightly higher; trainees who find the bottom too easy should lower the bar or elevate their feet.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Feet elevated inverted row | Greater bodyweight fraction; closer to BW pull-up difficulty | Progressive overload without external load |
| Suspension (TRX) inverted row | Unstable; handles rotate; increased stabilizer demand | Shoulder stabilizer training; travel/no-rack contexts |
| Wide-grip inverted row | Greater posterior delt and trap demand | Upper back width emphasis |
| Weighted vest inverted row | External load while maintaining closed-chain mechanics | Load progression beyond bodyweight |

> For system-specific training applications, see each system's lens entry.
