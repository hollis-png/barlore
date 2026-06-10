---
id: glute_ham_raise
name: Glute Ham Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 2

muscles:
  - id: biceps_femoris
    role: primary
  - id: semitendinosus
    role: primary
  - id: semimembranosus
    role: primary
  - id: gluteus_maximus
    role: secondary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary

# ebben_2009: Overall hamstrings 98% MVIC — highest activation of any leg curl variation tested.
# The GHR uniquely loads the hamstrings through BOTH knee flexion AND hip extension simultaneously,
# producing very high force demands on both proximal and distal hamstring attachment points.
muscle_activation_studies:
  - source_id: ebben_2009
    doi: null
    n: null
    population: "healthy adults, glute-ham raise machine"
    condition:
      implement: machine
      phase: full_rep
      notes: "Simultaneous knee flexion and hip extension; highest hamstring demand of any curl variation in this study"
    measurements:
      - {muscle: biceps_femoris, mean_pct_mvc: 98.0, sd: null}

joint_rom_required:
  knee_flexion_deg: 130
  hip_extension_deg: 30
  source: "ebben_2009"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Descending; hardest at the bottom of the rep (body horizontal, hamstrings maximally loaded through both joints); difficulty is front-loaded"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: moderate
    hip: low
  common_injuries:
    - structure: proximal_hamstring_tendon
      mechanism: eccentric_overload
      risk_factors: [attempting_without_adequate_strength, bodyweight_too_high_for_current_strength]
    - structure: distal_hamstring_tendon
      mechanism: eccentric_overload_at_knee
      risk_factors: [rapid_eccentric, insufficient_warm_up]
  contraindications:
    - acute_proximal_hamstring_tendinopathy
    - acute_posterior_knee_injury
    - insufficient_hamstring_strength_for_bodyweight

variations: []
progressions: []
alternatives: [lying_leg_curls, seated_leg_curl]

sources:
  - source_id: ebben_2009
    title: "Hamstring muscle EMG activity during various weight-bearing exercises"
    author: "Ebben, William P. et al."
    year: 2009
    doi: null
    credibility: rct
---

# Glute Ham Raise

The glute ham raise (GHR) produces the highest hamstring activation of any leg curl variation, approximately 98% MVIC in Ebben 2009. Unlike machine leg curls that load the hamstrings through knee flexion only, the GHR simultaneously demands both knee flexion and hip extension — forcing the hamstrings to contract forcefully across both of their attachment points at once. This dual-joint loading is why the GHR is exceptionally demanding and requires significant base hamstring strength.

## Execution

1. Adjust the GHR machine so the knees sit just behind the round pad, with feet secured against the footplate
2. Begin in the horizontal position (body parallel to the floor) — this is the starting position with hamstrings maximally loaded
3. Flex the knees to pull the body upward toward vertical while maintaining a neutral spine and driving the toes into the footplate
4. At the top, the body is approximately vertical with full knee flexion
5. Lower under complete control — the eccentric is the highest-risk portion

## What the EMG Data Shows

Ebben 2009:

| Exercise | Hamstring activation |
|----------|---------------------|
| GHR | 98% MVIC |
| Seated leg curl | 80.8% MVIC |
| Prone leg curl | 80% MVIC |

The near-maximal activation reflects the simultaneous demand on both the proximal (hip extension) and distal (knee flexion) functions of the hamstrings. No other isolation exercise matches this.

## Why the GHR Is Different from Leg Curls

| Feature | Machine Leg Curl | Glute Ham Raise |
|---------|-----------------|-----------------|
| Hip position | Fixed | Extends during rep |
| Knee flexion | Yes | Yes |
| Hamstring joints loaded | 1 (knee) | 2 (knee + hip) |
| Strength prerequisite | Low | High |

The GHR is appropriate for intermediate-to-advanced trainees with well-developed hamstring strength. Beginners should establish a base with machine leg curls first.

> For system-specific training applications, see each system's lens entry.
