---
id: pullups
name: Pull-Up
status: complete
category: exercise
pattern: [vertical_pull]
equipment: [bodyweight]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 1

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: infraspinatus
    role: primary
  - id: teres_major
    role: secondary
  - id: biceps_brachii
    role: secondary
  - id: trap_lower
    role: secondary
  - id: pectoralis_major
    role: secondary
  - id: deltoid_posterior
    role: secondary
  - id: rhomboids
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: external_oblique
    role: stabilizer

# ssd_2026 is a literature compilation (no single DOI) aggregating multiple EMG studies.
# Values for pronated pull-up: LD range 117–130% MVIC; midpoint 123.5 stored as mean.
# Chin-up data included as a separate condition for comparison, not as a separate exercise.
# No SD reported for erector_spinae and external_oblique (range only).
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: pronated
      width: shoulder-width
      notes: "Conventional pull-up"
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: 123.5, sd: null, notes: "Range 117–130% MVIC across studies"}
      - {muscle: biceps_brachii,   mean_pct_mvc: 78.0,  sd: 32.0}
      - {muscle: infraspinatus,    mean_pct_mvc: 79.0,  sd: 56.0}
      - {muscle: trap_lower,       mean_pct_mvc: 56.0,  sd: 21.0}
      - {muscle: pectoralis_major, mean_pct_mvc: 44.0,  sd: 27.0}
      - {muscle: erector_spinae,   mean_pct_mvc: 40.0,  sd: null, notes: "Isometric stabilization; range 39–41% MVIC"}
      - {muscle: external_oblique, mean_pct_mvc: 33.0,  sd: null, notes: "Isometric stabilization; range 31–35% MVIC"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: supinated
      width: shoulder-width
      notes: "Chin-up"
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: 117.0, sd: 46.0}
      - {muscle: biceps_brachii,   mean_pct_mvc: 96.0,  sd: 34.0}
      - {muscle: trap_lower,       mean_pct_mvc: 45.0,  sd: 22.0}
      - {muscle: pectoralis_major, mean_pct_mvc: 57.0,  sd: 36.0}

joint_rom_required:
  shoulder_flexion_deg: 180
  elbow_flexion_deg: 93.4
  elbow_flexion_chinup_deg: 100.6
  scapular_upward_rotation_deg: 60
  glenohumeral_contribution_deg: 120
  notes: >
    Full overhead shoulder flexion (180°) required to achieve dead-hang start.
    Chin-up requires greater terminal elbow flexion (100.6° vs 93.4°) because the
    supinated grip keeps the elbows in the sagittal plane, maximizing terminal ROM.
    Scapulothoracic joint contributes 60° of upward rotation; glenohumeral joint 120°.
  source: "ssd_2026"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: bottom_third
  notes: >
    Peak force generation occurs in the bottom third of the movement where the
    latissimus dorsi operates at its optimal length-tension relationship with its
    greatest moment arm. The primary sticking point is the top third, when the
    humerus is fully extended and adducted — the primary shoulder extensors suffer
    active insufficiency and secondary muscles must compensate to pull the chest to the bar.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: moderate
    elbow: low
  common_injuries:
    - structure: biceps_brachii_tendon
      mechanism: eccentric_overload_at_full_extension
      risk_factors: [excessive_eccentric_velocity, high_volume_fatigue, cold_muscles]
    - structure: glenohumeral_joint
      mechanism: impingement
      risk_factors: [inadequate_scapular_depression_at_top, kipping_technique, forward_head_posture]
    - structure: medial_elbow_common_flexor_tendon
      mechanism: repetitive_valgus_stress
      risk_factors: [wide_grip, high_frequency, insufficient_recovery]
  contraindications:
    - acute_biceps_tendon_rupture
    - shoulder_labral_tear_acute
    - medial_epicondylitis_acute

variations: []
progressions: [weighted_pull_ups]
alternatives: [chin_up]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Pull-Up

The pull-up is a closed-chain vertical pulling exercise in which the body hangs from a fixed overhead bar with a pronated (overhand) grip and is pulled upward until the chin clears the bar or the chest contacts it. As one of the few upper-body exercises that requires moving the entire bodyweight through a full range of motion against gravity, it serves as both a strength benchmark and a primary latissimus dorsi developer.

## Execution

1. Hang from the bar with a pronated (palms-away) double-overhand grip, hands approximately shoulder-width apart
2. Before initiating the pull, depress and retract the scapulae slightly — avoid passive hanging with the shoulders near the ears
3. Initiate the pull by driving the elbows down and back, thinking "elbows to hips" rather than "chin over bar"
4. Continue pulling until the chin clears the bar or the upper chest contacts it; maintain a slight backward lean throughout
5. Lower under control with a 2–3 second eccentric; do not drop from the top position

## What the EMG Data Shows

The pull-up produces among the highest latissimus dorsi activation of any exercise: 117–130% MVIC across studies compiled in the ssd_2026 literature review. Peak values at 130% MVIC are recorded on rotating-handle pull-up devices, where natural hand supination during the pull likely improves LD moment arm.

The infraspinatus (79% MVIC) is notably active as a dynamic glenohumeral stabilizer — not a prime mover, but essential for preventing superior humeral head migration under load. Lower trapezius (56% MVIC) acts as the primary scapular stabilizer throughout the movement.

The core contracts isometrically throughout: erector spinae 39–41% MVIC and external oblique 31–35% MVIC to suppress lower-body swinging and maintain pelvic alignment. This isometric trunk demand increases proportionally with bodyweight and with added external load.

## Pull-Up vs Chin-Up: What the Data Shows

Changing grip from pronated to supinated produces a distinct neuromuscular shift:

| Muscle | Pull-Up (pronated) | Chin-Up (supinated) |
|--------|-------------------|---------------------|
| Latissimus dorsi | 123.5% (117–130 range) | 117.0% ± 46.0 |
| Biceps brachii | 78.0% ± 32.0 | 96.0% ± 34.0 |
| Lower trapezius | 56.0% ± 21.0 | 45.0% ± 22.0 |
| Pectoralis major | 44.0% ± 27.0 | 57.0% ± 36.0 |

The chin-up is not a "biceps exercise disguised as a back exercise" — its latissimus dorsi activation (117% MVIC) is statistically equivalent to the pronated pull-up. The practical difference is that the chin-up provides a larger biceps brachii stimulus (+18% MVIC) while the pronated pull-up provides a larger lower trapezius stimulus (+11% MVIC). Neither variation is superior for lat development; selection should be based on which secondary muscles need more work.

## Strength Curve Implications

The descending strength curve — hardest at the top, easiest at the bottom — has direct programming implications. Strategies that address the sticking point in the top third:

- **Dead stop reps**: Pause 1 second at full extension before each rep; this starts every rep in the hardest position of the subsequent rep, forcing adaptation at the sticking point
- **Eccentric-focused reps**: Jump to the top and lower for 5–8 seconds; maximally loads the top-to-mid range under eccentric tension
- **Weighted pull-ups**: External load increases total force demand throughout, shifting the full range above the capability threshold and forcing strength adaptation at the sticking point

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Chin-up | Supinated grip; greater biceps demand | Biceps development; beginners (easier due to elbow mechanics) |
| Weighted pull-up | External load via belt or vest | Strength progression once bodyweight reps exceed 8–10 |
| Band-assisted pull-up | Band reduces effective bodyweight | Learning the movement pattern; increasing volume |
| Scapular pull-up | Arms straight throughout; scapula only | Isolating lower/mid trapezius and serratus; injury rehabilitation |

> For system-specific training applications, see each system's lens entry.
