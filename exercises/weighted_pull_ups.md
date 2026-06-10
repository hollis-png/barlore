---
id: weighted_pull_ups
name: Weighted Pull-Up
status: complete
category: exercise
pattern: [vertical_pull]
equipment: [bodyweight, dip_belt]

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

# EMG data from ssd_2026 (unweighted pronated pull-up). No weighted pull-up
# specific EMG %MVIC study found. Adding external load increases absolute force
# demand proportionally while preserving the relative muscle activation distribution —
# %MVIC values would remain similar or increase across all muscles.
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: pronated
      width: shoulder-width
      load: bodyweight_unweighted
      notes: "Unweighted baseline; weighted execution preserves this distribution at higher absolute force output"
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: 123.5, sd: null, notes: "Range 117–130% MVIC across studies"}
      - {muscle: biceps_brachii,   mean_pct_mvc: 78.0,  sd: 32.0}
      - {muscle: infraspinatus,    mean_pct_mvc: 79.0,  sd: 56.0}
      - {muscle: trap_lower,       mean_pct_mvc: 56.0,  sd: 21.0}
      - {muscle: pectoralis_major, mean_pct_mvc: 44.0,  sd: 27.0}
      - {muscle: erector_spinae,   mean_pct_mvc: 40.0,  sd: null, notes: "Isometric stabilization; increases with added load"}
      - {muscle: external_oblique, mean_pct_mvc: 33.0,  sd: null, notes: "Isometric stabilization; increases with added load"}

joint_rom_required:
  shoulder_flexion_deg: 180
  elbow_flexion_deg: 93.4
  scapular_upward_rotation_deg: 60
  glenohumeral_contribution_deg: 120
  notes: >
    Identical ROM requirements to the unweighted pull-up. Added load does not
    change the joint angles required; it only increases the force needed to move
    through them. Full overhead shoulder flexion (180°) required for the dead-hang start.
  source: "ssd_2026"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: bottom_third
  notes: >
    Same descending strength curve as the unweighted pull-up — peak force production
    in the bottom third where the latissimus dorsi has its greatest length-tension
    advantage, with a sticking point in the top third where active insufficiency
    of the primary shoulder extensors requires secondary muscle compensation.
    Added load shifts the entire force requirement upward, making the top third
    sticking point the limiting factor for load progression.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: high
    elbow: moderate
    lumbar: low
  common_injuries:
    - structure: biceps_brachii_tendon
      mechanism: eccentric_overload_at_full_extension
      risk_factors: [excessive_load_jump, fast_eccentric_descent, inadequate_warm_up]
    - structure: glenohumeral_joint
      mechanism: impingement
      risk_factors: [added_load_with_inadequate_scapular_control, kipping_with_weight, forward_head_posture]
    - structure: medial_elbow_common_flexor_tendon
      mechanism: repetitive_valgus_stress_amplified_by_load
      risk_factors: [wide_grip_with_heavy_weight, high_frequency, insufficient_recovery]
    - structure: lumbar_spine
      mechanism: compressive_load_from_dip_belt
      risk_factors: [heavy_loads_at_belt_attachment_point, pre_existing_disc_pathology]
  contraindications:
    - acute_biceps_tendon_rupture
    - shoulder_labral_tear_acute
    - medial_epicondylitis_acute

variations: [pullups, chin_up]
progressions: []
alternatives: [wide_grip_lat_pulldown, band_assisted_pull_up]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Weighted Pull-Up

The weighted pull-up is the primary strength progression from the bodyweight pull-up. External load is added via a dip belt (hanging plates or kettlebells), a weight vest, or a dumbbell held between the feet or ankles. The movement mechanics are identical to the unweighted pull-up; the added resistance increases the total force demand beyond what bodyweight alone can provide, driving continued strength adaptation once bodyweight reps plateau.

## Prerequisites

The weighted pull-up should not be attempted until the lifter can perform 8–10 consecutive clean bodyweight pull-ups — full dead hang at the bottom, chin over bar at the top, controlled eccentric. Attempting to add load before this threshold is established shifts the limiting factor from strength to technique and increases injury risk at the shoulder and elbow.

## Execution

1. Attach plates or a kettlebell to a dip belt; secure the belt around the hips with the weight hanging freely below
2. Hang from the bar with a pronated grip at approximately shoulder width; arms fully extended
3. Depress and slightly retract the scapulae before initiating the pull — do not begin from a passive shrug
4. Initiate by driving the elbows down and back ("elbows to hips"), not by curling the wrists toward the bar
5. Pull until the chin clears the bar or the upper chest contacts it
6. Lower under control for 2–3 seconds; do not drop from the top

## Load Selection and Progression

| Rep target at bodyweight | Starting added load | Notes |
|-------------------------|--------------------|----|
| 8–10 | 5–10 kg | Confirm technique is preserved before adding load |
| 10–12 | 10–15 kg | Speed of load increase should slow as absolute load rises |
| 15+ | 20+ kg | At this threshold, treat weighted pull-ups as a primary strength lift |

Small load increments (2.5–5 kg) are preferred over large jumps. The sticking point in the top third is exaggerated by added load — if technique breaks at the top before bodyweight pull-ups do, the load is too heavy.

## Dip Belt vs Weight Vest

| Method | Advantage | Disadvantage |
|--------|-----------|-------------|
| Dip belt with plates | Precise load adjustment; no body heat | Belt can shift; requires setup time |
| Weight vest | Evenly distributed; no setup | Load increments fixed by vest design; expensive |
| Dumbbell between feet/ankles | No equipment required | Limits range of motion; unstable |

The dip belt is the standard method for dedicated strength work and allows the most precise load progression.

## Relationship to Bodyweight Pull-Up

The weighted pull-up does not change the exercise — it changes the load. The ssd_2026 EMG data from unweighted pronated pull-ups represents the relative muscle activation distribution, which is preserved under load. What changes is absolute force output: at bodyweight + 20 kg, the latissimus dorsi is producing proportionally more absolute force than at bodyweight, even though the %MVIC distribution remains similar.

This is why weighted pull-ups are the logical final progression for vertical pulling — they overload the same movement pattern at higher absolute intensities without introducing technique variables.

> For system-specific training applications, see each system's lens entry.
