---
id: floor_press
name: Floor Press
status: complete
category: exercise
pattern: [horizontal_push]
equipment: [barbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: triceps_brachii
    role: primary
  - id: pectoralis_major
    role: secondary
  - id: deltoid_anterior
    role: secondary

# ebd_2026 literature compilation. All activation data is qualitative — no specific
# %MVIC values reported. Relative descriptions preserved as notes.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      surface: floor
      phase: full_rep
    measurements:
      - {muscle: triceps_brachii,  mean_pct_mvc: null, notes: "Dominant throughout; especially high during concentric drive from dead stop with no stretch reflex"}
      - {muscle: pectoralis_major, mean_pct_mvc: null, notes: "Reduced vs full bench press — floor eliminates bottom stretch and stretch-shortening contribution"}
      - {muscle: deltoid_anterior,  mean_pct_mvc: null, notes: "Highly active during initial concentric ascent phase"}

joint_rom_required:
  shoulder_extension_deg: 0
  elbow_flexion_deg: 90
  notes: >
    Shoulder extension strictly limited to 0° — the floor blocks posterior humerus
    travel. Elbow flexion limited to ~90° when upper arms contact the floor. The
    combination eliminates the bottom third of the standard bench press ROM.
  source: "ebd_2026"

strength_curve:
  type: ascending
  sticking_point: bottom
  peak_force_position: lockout
  notes: >
    Sticking point is immediately off the floor — no stretch reflex available.
    All force production is purely concentric. Operates exclusively in the mechanically
    stronger mid-range and lockout portion of the pressing curve. Pause before pressing
    is recommended to fully dissipate stored elastic energy.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
    wrist: low
  common_injuries:
    - structure: elbow_soft_tissue
      mechanism: impact
      risk_factors: [slamming_elbows_into_floor, uncontrolled_descent]
    - structure: wrist
      mechanism: hyperextension
      risk_factors: [uncontrolled_bar_drop, excessively_heavy_load]
  contraindications: []

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

# Floor Press

The floor press is a horizontal pressing variation performed lying supine on the floor rather than on an elevated bench. The floor acts as a hard stop, limiting shoulder extension to 0° (arms parallel to the floor) and restricting elbow flexion to approximately 90° when the upper arms contact the ground. This eliminates the bottom third of the standard bench press range of motion.

## Execution

1. Set J-hooks low in a power rack; lie underneath with the bar above the mid-chest
2. Grip at standard bench press width; keep shoulder blades retracted and depressed against the floor
3. Unrack and begin the descent; lower the bar until the triceps touch the floor — do not bounce
4. Pause for 1 second with full weight suspended; this dissipates elastic energy and converts the lift to pure concentric
5. Drive the bar upward by extending the elbows; keep the bar directly over the mid-chest

## What the Data Shows

The floor press data from ebd_2026 is qualitative — no specific %MVIC values are reported. The key findings are comparative:

**Triceps dominance**: The triceps brachii is the dominant muscle throughout the lift, especially during the concentric drive from the dead-stop position. Because the stretch-shortening cycle is unavailable at the bottom, the triceps cannot rely on elastic energy transfer — all force must come from active contractile effort.

**Reduced pectoralis major**: The floor press structurally prevents the pectoralis major from reaching its fully stretched state at the bottom. This reduces the elastic contribution of the pec and lowers overall pec activation compared to a full-ROM bench press. The floor press is therefore not primarily a chest exercise.

**Anterior deltoid**: Highly active during the initial concentric ascent phase, functioning as a key prime mover alongside the triceps.

## The Design Purpose

The floor press was originally used by powerlifters to address mid-range and lockout weaknesses. By eliminating leg drive and the stretch reflex, it isolates the concentric pressing capacity without the mechanical boost that full bench press technique provides. Bodybuilders use it for elbow-tendon management — the restricted ROM reduces tendon stress at the shoulder while allowing heavy triceps loading.

The floor press is also one of the safest pressing exercises for athletes with shoulder pathology: by restricting extension to 0°, it eliminates the anterior shoulder impingement risk associated with deep shoulder extension in the full bench press.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Dumbbell floor press | Independent arm path; greater ROM flexibility | Unilateral assessment; shoulder management |
| Close-grip floor press | Narrow grip + floor ROM restriction | Maximum triceps overload with minimal shoulder risk |
| Full bench press | Full ROM; stretch reflex available | Primary horizontal pressing development |

> For system-specific training applications, see each system's lens entry.
