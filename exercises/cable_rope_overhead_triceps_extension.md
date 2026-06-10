---
id: cable_rope_overhead_triceps_extension
name: Cable Rope Overhead Triceps Extension
status: complete
category: exercise
pattern: [isolation]
equipment: [cable]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 2

muscles:
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary

# boehler_2011 (normalized to triangle push-up, NOT true %MVIC):
#   triceps_long 81% ± 21.4%, triceps_lateral 72% ± 16.5%.
# Highest long head activation in boehler_2011 among all exercises tested (tied with rope pushdown).
# Shoulder at 180° (overhead) → triceps long head at maximum length.
muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults, rope attachment overhead"
    condition:
      implement: cable_rope
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Shoulder at ~180° flexion overhead."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 81.0, sd: 21.4}
      - {muscle: triceps_lateral, mean_pct_mvc: 72.0, sd: 16.5}

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_flexion_deg: 180
  source: "boehler_2011"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: top
  notes: "Descending; hardest when elbows are most flexed behind the head (maximum triceps stretch); cable provides constant tension throughout"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: moderate
  common_injuries:
    - structure: triceps_tendon_long_head
      mechanism: stretch_overload
      risk_factors: [forcing_too_much_elbow_flexion_behind_head, heavy_load, pre_existing_triceps_tendinopathy]
    - structure: posterior_shoulder_capsule
      mechanism: passive_stretch
      risk_factors: [limited_shoulder_flexion_mobility, forced_overhead_position]
  contraindications:
    - acute_triceps_long_head_tendinopathy
    - severe_shoulder_flexion_restriction

variations: []
progressions: []
alternatives: [ez_bar_skullcrusher, lying_triceps_press]

sources:
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
---

# Cable Rope Overhead Triceps Extension

The cable rope overhead triceps extension places the shoulder at approximately 180° flexion (fully overhead) and extends the elbow against the cable resistance. This overhead shoulder position takes the triceps long head — which crosses the shoulder joint — to its maximum mechanical length, producing the highest long head activation stimulus among triceps isolation exercises. The cable provides constant tension, including at the bottom of the range where the triceps is most stretched.

## Execution

1. Attach a rope to a low cable pulley; face away from the stack
2. Grasp the rope with both hands behind the head, shoulder fully overhead, elbows bent and pointing forward
3. Extend the elbows to push the rope upward until the arms are straight overhead
4. Lower under control until the forearms are fully behind the head at maximum stretch
5. Keep the upper arms close to the sides of the head throughout — do not let the elbows flare

## What the EMG Data Shows

Boehler 2011 (normalized to triangle push-up, not %MVIC):

| Exercise | Triceps Long | Triceps Lateral |
|----------|-------------|-----------------|
| Overhead cable extension | 81 ± 21.4 | 72 ± 16.5 |
| Rope pushdown | 81 ± 32.3 | 67 ± 15.7 |
| Skullcrusher | 70 ± 20.9 | 55 ± 14.1 |
| Kickback | 88 ± 33.0 | 87 ± 23.7 |

The overhead position ties the pushdown for long head activation in normalized terms, with notably less variance (SD 21.4 vs 32.3). The key advantage over the pushdown is the overhead position places the long head at its maximum length.

## Why the Overhead Position Matters

The triceps long head originates at the infraglenoid tubercle of the scapula (shoulder). When the arm is raised overhead (shoulder at 180°), the long head is stretched at the proximal end simultaneously with elbow flexion stretching it at the distal end. This dual-stretch produces the maximum elongation available for the long head — which constitutes approximately 60% of triceps volume.

Programs that rely entirely on pushdowns and skullcrushers underload the long head's lengthened range. The overhead extension addresses this gap.

## Cable vs Dumbbell Overhead Extension

The cable provides constant tension at the most stretched position (elbows maximally bent behind the head), where a dumbbell would have near-zero effective resistance at that angle. For maximizing the lengthened-range stimulus, the cable overhead extension is mechanically superior to the dumbbell version.

> For system-specific training applications, see each system's lens entry.
