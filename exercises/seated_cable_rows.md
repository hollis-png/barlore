---
id: seated_cable_rows
name: Seated Cable Rows
status: complete
category: exercise
pattern: [horizontal_pull]
equipment: [cable]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: trap_middle
    role: primary
  - id: trap_lower
    role: primary
  - id: deltoid_posterior
    role: secondary
  - id: biceps_brachii
    role: secondary
  - id: rhomboids
    role: secondary
  - id: erector_spinae
    role: stabilizer

# ssd_2026 literature compilation. No absolute %MVIC values reported.
# Data is comparative (narrow vs wide grip, fixed vs free scapular) with effect sizes.
# Do NOT fabricate numeric %MVIC values. Effect sizes stored as notes.
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: 14
    population: "resistance-trained men, 8-RM load, HD-sEMG"
    condition:
      variation: narrow_grip
      shoulder_abduction_deg: 0
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: null, notes: "Significantly greater than wide grip, concentric and eccentric (ES = 1.08)"}
      - {muscle: biceps_brachii,   mean_pct_mvc: null, notes: "Maximized at 0° abduction (supinated, neutral, or pronated narrow grip)"}
  - source_id: ssd_2026
    doi: null
    n: 14
    population: "resistance-trained men, 8-RM load, HD-sEMG"
    condition:
      variation: wide_grip
      shoulder_abduction_deg: 90
    measurements:
      - {muscle: trap_middle,       mean_pct_mvc: null, notes: "Significantly greater than narrow grip, concentric ES = 1.35, eccentric ES = 2.79"}
      - {muscle: trap_lower,         mean_pct_mvc: null, notes: "Significantly greater than narrow grip; same ES pattern as trap_middle"}
      - {muscle: deltoid_posterior,  mean_pct_mvc: null, notes: "Significantly greater than narrow grip; lateral deltoid ES = 1.35"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: fixed_scapular_row
      notes: "Scapular movement restricted throughout the set"
    measurements:
      - {muscle: deltoid_posterior, mean_pct_mvc: null, notes: "Significantly increased during concentric phase vs free scapular row (ES = 0.66)"}
      - {muscle: trap_middle,        mean_pct_mvc: null, notes: "Significantly increased during eccentric phase vs free scapular row (ES = 0.67)"}
      - {muscle: latissimus_dorsi,  mean_pct_mvc: null, notes: "Significantly increased during eccentric phase vs free scapular row (ES = 0.85)"}

joint_rom_required:
  shoulder_flexion_start_deg: 90
  elbow_flexion_deg: 110
  notes: >
    Movement begins with shoulders at ~90° flexion (arms extended forward). Concentric
    phase drives the shoulder from flexion through horizontal extension to neutral (0°
    for narrow grip; up to 90° abduction for wide grip). Elbows flex 90–110° at the
    terminal contraction. Torso remains upright with a neutral lumbar spine throughout.
  source: "ssd_2026"

strength_curve:
  type: ascending_descending
  sticking_point: terminal_lockout
  peak_force_position: mid_range
  notes: >
    Bell-shaped (ascending-descending) curve. Peak resistance at mid-range when the
    elbow is flexed ~90° and the shoulder is in neutral extension — optimal moment arm
    for both LD and trapezius. Sticking point is terminal lockout where the handle
    meets the torso: the horizontal lever arm shortens and scapular retraction must be
    completed against a compressed range. Cable maintains near-constant tension at
    full arm extension, unlike free-weight rows which lose tension at that position.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
    lower_back: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: excessive_forward_torso_lean_at_start
      risk_factors: [torso_lean_beyond_30_deg, heavy_loads, fatigue]
    - structure: shoulder_rotator_cuff
      mechanism: impingement_at_terminal_retraction
      risk_factors: [excessively_wide_grip, forced_scapular_retraction_at_end_range]
  contraindications: []

variations: []
progressions: []
alternatives: [bent_over_barbell_row, inverted_row]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Seated Cable Rows

The seated cable row is an open-chain horizontal pulling exercise performed on a low-pulley cable machine. The seated position eliminates hip hinge mechanics and spinal erector loading, directing the stimulus entirely to the upper back, mid-trapezius, and posterior shoulder. Constant cable tension provides resistance throughout the full ROM — unlike free weights, which lose tension as the lever arm shortens at lockout. Grip width and shoulder abduction angle are the primary variables that shift load between the latissimus dorsi (narrow) and trapezius/posterior deltoid (wide).

## Execution

1. Sit at the machine with feet flat on the platform, knees slightly bent; grip the attachment at shoulder width or narrower
2. Begin with the torso upright and arms fully extended, cable taut — do not lean back beyond ~10° to initiate the pull
3. Pull the handle toward the lower sternum, driving the elbows behind the torso and retracting the scapulae
4. Pause briefly at full retraction; return the handle under control to full arm extension
5. Allow the scapulae to protract at the end of the eccentric — do not hold them pinned throughout the set

## What the Data Shows

The seated cable row data from ssd_2026 is comparative — no absolute %MVIC values are reported. The findings are effect sizes from a 14-person HD-sEMG study at 8-RM.

**Narrow grip (0° shoulder abduction)** produces significantly greater latissimus dorsi activation across both concentric and eccentric phases (ES = 1.08 vs wide grip). Biceps brachii is also maximized at narrow grip angles. The narrow-grip cable row is the preferred variant for LD development.

**Wide grip (90° shoulder abduction)** produces significantly greater activation of the middle and lower trapezius (concentric ES = 1.35, eccentric ES = 2.79) and posterior/lateral deltoid (ES = 1.35). The wide-grip cable row is primarily a rear-delt and trap exercise.

**Fixed vs free scapular movement** changes target muscle emphasis across phases. Restricting scapular movement increases posterior deltoid in the concentric phase (ES = 0.66) and traps + LD in the eccentric phase (ES = 0.85–0.67). Free scapular movement distributes load evenly and reinforces normal scapulohumeral coordination — preferred for long-term shoulder health. Fixed scapular technique can be used selectively for eccentric trap or LD isolation emphasis.

## Grip Width Selection

| Goal | Grip | Shoulder abduction |
|------|------|--------------------|
| LD hypertrophy | Narrow (V-bar, supinated) | 0° |
| Upper/mid trap | Wide (straight bar, pronated) | 60–90° |
| Rear delt | Wide + fixed scapula | 90° |
| General back | Neutral narrow | 0° |

## Constant Tension Advantage

Free-weight rows (barbell, dumbbell) lose resistance at full arm extension because the moment arm collapses when the weight stack reaches its lowest point relative to the shoulder. The cable maintains near-constant tension throughout, including at the fully stretched position. This makes the seated cable row superior for training the stretched lengthened position of the LD and trapezius — where mechanosensitive hypertrophy signaling is highest per recent stretch-mediated hypertrophy research.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Bent-over barbell row | Free weight; erector loading; heavier loads | Athletic strength; spinal erector training |
| Inverted row | Bodyweight; closed-chain; spinal unloading | Rehabilitation; bodyweight training |
| Single-arm cable row | Unilateral; greater ROM; anti-rotation core | Asymmetry correction; core integration |
| Face pull | High cable position; external rotation emphasis | Posterior cuff and rear delt isolation |

> For system-specific training applications, see each system's lens entry.
