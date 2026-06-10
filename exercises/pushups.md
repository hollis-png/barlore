---
id: pushups
name: Pushups
status: complete
category: exercise
pattern: [horizontal_push]
equipment: [bodyweight]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: pectoralis_major
    role: primary
  - id: triceps_brachii
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: serratus_anterior
    role: stabilizer
  - id: rectus_abdominis
    role: stabilizer
  - id: external_oblique
    role: stabilizer

# ebd_2026 literature compilation.
# Standard pushup values are ranges (95–105% PM; 73–109% TB; 67–87% SA).
# Midpoints stored as mean_pct_mvc; actual ranges preserved as notes.
# Bodyweight load (~68% on hands) is a kinematic load value, not %MVIC.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: standard
      hand_width: shoulder-width
    measurements:
      - {muscle: pectoralis_major,  mean_pct_mvc: 100, sd: null, notes: "Range 95–105% MVIC; higher in diamond and TRX variations"}
      - {muscle: triceps_brachii,   mean_pct_mvc: 91,  sd: null, notes: "Range 73–109% MVIC; higher in diamond variations"}
      - {muscle: serratus_anterior, mean_pct_mvc: 77,  sd: null, notes: "Range 67–87% MVIC; primary scapular protractor"}
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: diamond
      hand_width: close
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: null, notes: "Highest relative EMG across standard/diamond/wide hand positions"}
      - {muscle: triceps_brachii,  mean_pct_mvc: null, notes: "Highest relative EMG across standard/diamond/wide hand positions"}

joint_rom_required:
  elbow_flexion_deg: null
  shoulder_abduction_deg: null
  notes: >
    Elbows tucked 45–70° relative to torso for shoulder safety (not fully flared).
    Chest lowers until close to the floor. Standard pushup supports ~68% of total
    bodyweight on the hands throughout the movement.
  source: "ebd_2026"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: >
    Hardest at the bottom where the pec is maximally stretched and chest is near the floor.
    Mechanical demand decreases as the elbows extend. The concentric phase produces higher
    raw RMS EMG than the eccentric phase, confirming the primary training stimulus
    is in the pressing phase.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: low
    wrist: moderate
    elbow: low
  common_injuries:
    - structure: wrist_extensor_tendons
      mechanism: repetitive_dorsiflexion_under_load
      risk_factors: [high_volume, inadequate_wrist_preparation, hard_floor]
    - structure: shoulder_subacromial_space
      mechanism: impingement
      risk_factors: [fully_flared_elbows_beyond_70_deg, excessively_wide_hand_placement]
  contraindications:
    - acute_wrist_tendinopathy
    - distal_radius_fracture_acute

variations: []
progressions: []
alternatives: []

sources:
  - source_id: ebd_2026
    title: "Exercise Biomechanics Data Extraction: Upper Push Accessories"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Pushups

The pushup is a closed-chain bodyweight pressing exercise performed in a prone plank position. It is the most accessible upper-body pressing movement, requiring no equipment and supporting approximately 68% of total bodyweight through the hands. EMG analysis confirms the pushup elicits pectoralis major activation (95–105% MVIC) comparable to a bench press loaded at approximately 60% of 1RM — making it a meaningful training stimulus across a wide range of populations.

## Execution

1. Place hands slightly wider than shoulder-width; fingers pointing forward or 15° outward
2. Set a rigid plank from head to heel — no hip sag or pike; brace the core throughout
3. Lower the chest toward the floor with elbows at 45–70° from the torso (not fully flared)
4. Touch or approach the floor; pause briefly
5. Press through both hands simultaneously until the elbows are straight; actively protract (push) the scapulae at the top

## What the EMG Data Shows

**Pectoralis major (95–105% MVIC)**: Standard pushups produce near-maximal pec activation despite supporting only 68% of bodyweight. This is equivalent to a bench press loaded at ~60% 1RM — the pec is under significant loading without requiring external load.

**Triceps brachii (73–109% MVIC)**: The wide range reflects variation in hand width and execution. Diamond pushups (hands close under chest) push triceps activation toward the upper end; standard pushups cluster in the mid-range.

**Serratus anterior (67–87% MVIC)**: This is the pushup's differentiating feature from the bench press. The bench press pins the scapulae to the pad, suppressing serratus anterior activity. The pushup requires active scapular protraction throughout, generating substantial serratus activation — a major contributor to serratus health and long thoracic nerve function. The pushup is the primary exercise prescribed for serratus anterior strengthening in rehabilitation.

**Diamond pushup superiority**: The diamond (triangle) hand position produces the highest relative EMG for both the pectoralis major and triceps brachii across all hand widths, making it the most demanding standard-surface pushup variation.

## The Scapular Advantage

The pushup's key mechanical distinction from all forms of bench pressing is scapular freedom. Because the chest is not anchored to a pad, the scapulothoracic joint can move through full protraction and retraction throughout each rep. This creates:

1. Active serratus anterior strengthening (67–87% MVIC) — unavailable in the bench press
2. Natural scapulohumeral rhythm — the glenohumeral joint is not exposed to impingement positions created by forcible scapular pinning
3. Core demand — the entire chain from feet to hands must remain rigid, unlike the supine bench position

For populations prioritizing shoulder health over maximum load, the pushup is often superior to the bench press despite lower absolute loading.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Diamond pushup | Narrow hands; highest triceps and pec EMG | Triceps emphasis; maximum bodyweight pressing demand |
| Wide pushup | >shoulder width hands; greater pec horizontal adduction | Pec major width emphasis |
| Pushup on rings/TRX | Unstable; significantly increases pec and core activation | Pec emphasis; serratus and shoulder stabilizer demand |
| Archer pushup | Asymmetric; loads one arm progressively | Progression toward one-arm pushup |

> For system-specific training applications, see each system's lens entry.
