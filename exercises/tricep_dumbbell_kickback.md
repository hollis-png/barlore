---
id: tricep_dumbbell_kickback
name: Tricep Dumbbell Kickback
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary

# boehler_2011 (normalized to triangle push-up, NOT true %MVIC):
#   triceps_long 88% ± 33.0%, triceps_lateral 87% ± 23.7%.
# HIGHEST relative values in boehler_2011, BUT with the largest SD (33%).
# Ascending strength curve: near-zero resistance at start (elbow 90°, forearm vertical),
# maximum only at full extension (arm horizontal). Effective load at peak contraction is low.
muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults, bent-over kickback"
    condition:
      implement: dumbbell
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Ascending curve: near-zero effective load at start."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 88.0, sd: 33.0}
      - {muscle: triceps_lateral, mean_pct_mvc: 87.0, sd: 23.7}

joint_rom_required:
  elbow_flexion_deg: 90
  shoulder_extension_deg: 20
  hip_flexion_deg: 90
  source: "boehler_2011"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "SEVERE gravity mismatch — maximum resistance only when arm is extended and horizontal; near-zero resistance at the start (elbow 90°, forearm vertical)"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: low
    lower_back: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: prolonged_hip_flexion_with_load
      risk_factors: [heavy_dumbbells, sustained_bent_over_position, pre_existing_lumbar_pathology]
  contraindications:
    - acute_lumbar_disc_herniation

variations: []
progressions: []
alternatives: [triceps_pushdown, cable_rope_overhead_triceps_extension]

sources:
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
---

# Tricep Dumbbell Kickback

The dumbbell kickback is performed bent over with the upper arm held parallel to the floor, extending the forearm backward (toward the ceiling) against gravity. Boehler 2011 reports the highest normalized values among all triceps exercises tested — but this is largely an artifact of the ascending strength curve: the triceps is most activated at full extension, which is also the position of highest gravitational resistance. However, the effective load through most of the range is extremely low because gravity provides near-zero resistance when the forearm is vertical.

## Execution

1. Hold a dumbbell in one hand; place the opposite hand and knee on a bench for support
2. Raise the upper arm until it is parallel to the floor and close to the torso
3. Start with the forearm pointing down (elbow at ~90°)
4. Extend the elbow until the arm is fully extended and horizontal
5. Lower under control; do not allow the elbow to swing

## What the EMG Data Shows

Boehler 2011 normalized values:

| Exercise | Triceps Long | Triceps Lateral |
|----------|-------------|-----------------|
| Kickback | **88 ± 33.0** | **87 ± 23.7** |
| Overhead cable ext. | 81 ± 21.4 | 72 ± 16.5 |
| Rope pushdown | 81 ± 32.3 | 67 ± 15.7 |
| Skullcrusher | 70 ± 20.9 | 55 ± 14.1 |

These are the highest normalized values but the SD of 33% for the long head is the largest of any exercise. This reflects the severe load variability across subjects and the ascending curve's inconsistency.

## The Fundamental Limitation: Gravity Mismatch

The kickback's ascending strength curve creates a mechanical paradox:
- At the starting position (elbow 90°, forearm vertical): gravity applies near-zero torque — the triceps does almost no work
- Only at full extension (arm horizontal) does maximum gravitational resistance apply
- Only the last few degrees of extension are meaningfully loaded

The result: most of the rep is performed against negligible resistance. A cable pushdown or overhead extension loads the triceps throughout the entire range.

## When Kickbacks Are Useful

- **End-of-session finisher**: Very high rep sets (20–30) with light load accumulate metabolic stress at peak contraction
- **Proprioception and isolation practice**: The joint-fixed position trains clean elbow extension technique
- **Situations without cable access**: When only dumbbells are available

For primary triceps development, pushdowns and overhead extensions provide superior load application.

> For system-specific training applications, see each system's lens entry.
