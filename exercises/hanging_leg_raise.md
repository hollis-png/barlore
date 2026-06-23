---
id: hanging_leg_raise
name: Hanging Leg Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [pull_up_bar]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 2

muscles:
  - id: rectus_abdominis
    role: primary
  - id: iliopsoas
    role: primary
  - id: external_oblique
    role: secondary
  - id: rectus_femoris
    role: secondary

muscle_activation_studies:
  - source_id: mcgill_2015
    doi: "10.1080/02640414.2014.946437"
    n: null
    population: "healthy young adult males"
    condition:
      load_pct_1rm: null
      implement: "pull-up bar"
      phase: dynamic
      notes: "Hanging straight leg raise to 90°. Generates ~3000 N spinal compression — highest anterior chain compressive load in the study. MVC normalization."
    measurements:
      - muscle: rectus_abdominis
        mean_pct_mvc: 130.0
        sd: null
      - muscle: external_oblique
        mean_pct_mvc: 88.0
        sd: null

joint_rom_required:
  hip_flexion_deg: 90
  shoulder_flexion_deg: 180
  source: "McGill et al. 2015"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Hip flexor moment arm is maximal at 90° (legs horizontal); force demand increases from 0° to 90°, then decreases as legs travel past horizontal toward the bar. Sticking point at the horizontal leg position."
  source: "biomechanical inference; McGill et al. 2015"

injury_risk:
  joint_stress:
    lumbar: moderate
    shoulder: low
  common_injuries:
    - structure: lumbar_spine
      mechanism: compressive_load
      risk_factors: [straight_leg_raise_at_high_repetitions, pre_existing_disc_pathology, lumbar_stenosis]
    - structure: shoulder_joint
      mechanism: distraction_force
      risk_factors: [extended_hang_duration, rotator_cuff_weakness]
  contraindications:
    - acute_lumbar_disc_herniation
    - acute_shoulder_instability

variations: []
progressions: []
alternatives: []

sources:
  - title: "Muscle activity and spine load during anterior chain whole body linkage exercises: the body saw, hanging leg raise and walkout from a push-up"
    author: "McGill, S. M., Andersen, J., & Cannon, J."
    year: 2015
    doi: "10.1080/02640414.2014.946437"
    source_id: mcgill_2015
    credibility: rct
---

# Hanging Leg Raise

The hanging leg raise is performed by hanging from a pull-up bar and raising the legs to horizontal using the hip flexors and abdominal muscles. McGill et al. (2015) identified it as one of the highest anterior chain challenges available, generating rectus abdominis activation of 130% MVC — exceeding the normalization reference value. This high activation comes with a significant trade-off: approximately 3000 N of spinal compressive force, the highest of any common core exercise studied.

## Execution

1. Hang from a pull-up bar with arms fully extended, grip slightly wider than shoulder width
2. Depress the scapulae and brace the core before initiating the movement
3. Raise the legs by flexing at the hip — keep the knees extended for maximum difficulty
4. Raise until the legs are parallel to the floor (90° hip flexion); pause briefly
5. Lower under control, resisting the eccentric with the hip flexors and abdominals

## Why Activation Exceeds 100% MVC

Values above 100% MVC indicate that the dynamic demand of the exercise exceeds the force produced during the isolated isometric normalization test. This occurs when the stretch-shortening cycle, momentum, or eccentric demands exceed a simple isometric maximum. It reflects high dynamic challenge, not measurement error.

## Spinal Compression Trade-Off

| Exercise | Spinal Compression | Rectus Abdominis |
|---|---|---|
| Hanging straight leg raise | ~3000 N | 130% MVC |
| Suspension body saw | <2500 N | ~58% MVC |
| Front plank | Low | ~48% MVC |

For athletes with lumbar disc pathology or stenosis, lower-compression alternatives (ab wheel rollout, body saw, plank progressions) should be prioritised. For healthy athletes, the hanging leg raise is a high-yield core exercise.

## Regression / Progression

| Level | Exercise |
|-------|----------|
| Beginner | Hanging knee raise (shorter lever arm, lower compression) |
| Intermediate | Hanging leg raise to 90° |
| Advanced | Toes-to-bar (full hip flexion range) |

> For system-specific training applications, see each system's lens entry.
