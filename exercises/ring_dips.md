---
id: ring_dips
name: Ring Dips
status: complete
category: exercise
pattern: [vertical_push]
equipment: [gymnastic_rings]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 4
  mobility_prerequisite: 2

muscles:
  - id: triceps_brachii
    role: primary
  - id: pectoralis_major
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: serratus_anterior
    role: stabilizer
  - id: latissimus_dorsi
    role: stabilizer
  - id: trap_lower
    role: stabilizer

# ebd_2026 literature compilation.
# Triceps peak: 1.05 ± 0.27 mV (raw millivolts) — NOT stored as mean_pct_mvc because
#   raw mV values are not normalized and cannot be compared across subjects or exercises.
#   This value is reported in the prose for comparison with bar dip (1.04 ± 0.27 mV).
# Pectoralis major: qualitative only ("extremely high").
# Stabilizers: qualitative increase with fatigue.
# Shoulder extension ROM is the primary quantitative kinematic measure.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      apparatus: gymnastic_rings
      phase: full_rep
    measurements:
      - {muscle: triceps_brachii,   mean_pct_mvc: null, notes: "Peak 1.05 ± 0.27 mV (raw mV, not %MVIC; equivalent to bar dip 1.04 ± 0.27 mV)"}
      - {muscle: pectoralis_major,  mean_pct_mvc: null, notes: "Extremely high — functions as primary adductor to prevent rings from flaring outward"}
      - {muscle: serratus_anterior, mean_pct_mvc: null, notes: "Increases significantly with fatigue to maintain ring stability"}
      - {muscle: trap_lower,         mean_pct_mvc: null, notes: "Increases significantly with fatigue as primary compensatory stabilizer"}
      - {muscle: latissimus_dorsi,   mean_pct_mvc: null, notes: "Increases significantly with fatigue; secondary adduction stabilizer"}

joint_rom_required:
  shoulder_extension_deg: 61.72
  elbow_flexion_deg: 90
  notes: >
    Peak shoulder extension 61.72° ± 13.51° — significantly less than parallel bar dip
    (78.20° ± 9.84°) due to ring instability limiting depth. Elbows maintained at ~90°
    at the bottom. Forearms must remain vertical to prevent ring drift and shoulder strain.
  source: "ebd_2026"

strength_curve:
  type: descending_to_flat
  sticking_point: bottom_and_lockout
  peak_force_position: eccentric_concentric_transition
  notes: >
    Bottom position remains highly demanding (descending curve portion). At lockout,
    a secondary sticking point appears: the lifter must generate substantial adduction
    force to prevent rings from drifting laterally, reducing the mechanical advantage
    normally present at full elbow extension in a stable bar dip.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: moderate
    elbow: moderate
    wrist: moderate
  common_injuries:
    - structure: glenohumeral_joint
      mechanism: uncontrolled_shoulder_loads_from_ring_instability
      risk_factors: [inadequate_ring_control_skill, fatigue, wide_ring_spacing]
    - structure: elbow_ligaments
      mechanism: valgus_or_varus_stress_from_ring_drift
      risk_factors: [inadequate_ring_control_skill, fatigue, excessive_elbow_flare]
    - structure: wrist_extensors
      mechanism: forced_dorsiflexion_under_load
      risk_factors: [inadequate_wrist_preparation, excessive_ring_distance_from_body]
  contraindications:
    - anterior_shoulder_instability
    - acute_elbow_ligament_injury

variations: [parallel_bar_dip]
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

# Ring Dips

The ring dip is an advanced bodyweight pressing exercise performed on gymnastic rings suspended from an overhead anchor. Unlike the stable parallel bar dip, the rings can move freely in three dimensions. This structural instability forces the pectoralis major to function as a primary adductor throughout the movement — preventing the rings from drifting laterally — while the rotator cuff, serratus anterior, lower trapezius, and latissimus dorsi must co-contract continuously to maintain ring position.

## Execution

1. Mount the rings; lock the elbows and externally rotate the wrists so palms face inward-forward; rings should be tight to the body
2. Brace the core; keep feet together or crossed behind
3. Lower by flexing the elbows; keep the rings close and forearms vertical to prevent ring drift
4. Descend until the elbows reach 90°; do not chase depth — ring instability limits safe extension to ~62° of shoulder extension vs 78° for bar dips
5. Drive through the rings to lockout; at the top, actively close the rings slightly toward each other to prevent flaring

## What the Data Shows

**Triceps activation is equivalent to the parallel bar dip**: Ring dip triceps peak activation is 1.05 ± 0.27 mV vs 1.04 ± 0.27 mV for the bar dip — statistically identical. Despite their dramatically different difficulty profiles, the ring dip does not produce greater triceps activation than the bar dip.

**Pectoralis major is the differentiating factor**: The pec is described as "extremely high" in the ring dip — but not for the same reason as in the bar dip. In the bar dip, the pec works as a shoulder extensor and flexor during the pressing movement. In the ring dip, the pec must also contract continuously as an adductor to prevent the rings from drifting, adding an independent component of pec demand that doesn't exist in bar dip.

**Stabilizers escalate under fatigue**: As ring dip sets progress, the serratus anterior, lower trapezius, and latissimus dorsi show significantly increased EMG amplitude. This is the nervous system recruiting additional stabilizers to compensate for degrading ring control — a phenomenon that does not occur in stable bar dips. This fatigue response is both the mechanism of ring dip's additional demand and the primary injury risk factor.

## Ring Dip vs Parallel Bar Dip

| Feature | Parallel Bar Dip | Ring Dip |
|---------|-----------------|----------|
| Shoulder extension ROM | 78.20° ± 9.84° | 61.72° ± 13.51° |
| Triceps peak activation | 1.04 ± 0.27 mV | 1.05 ± 0.27 mV |
| Pectoralis major demand | High (extensors + flexors) | Extremely high (+adduction) |
| Stabilizer demand at lockout | Low | High (prevents ring drift) |
| Strength curve | Descending, clear lockout | Descending-to-flat |

The ring dip is not simply a "harder dip." It is a qualitatively different movement that trains ring stabilization as a primary skill. Its reduced shoulder extension ROM (62° vs 78°) actually makes the bottom position safer for the anterior shoulder, but the unpredictable ring drift creates higher peak joint loads during loss of control. The prerequisite is competence at 3× 10 bodyweight bar dips before attempting ring dips.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Parallel bar dip | Stable; greater shoulder extension ROM | Primary pressing strength |
| Ring support hold | No dipping; isometric ring stabilization | Building ring control prerequisite |
| Weighted ring dip | External load; extremely high difficulty | Gymnastic strength beyond bodyweight |

> For system-specific training applications, see each system's lens entry.
