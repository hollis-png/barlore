---
id: push_press
name: Push Press
status: complete
category: exercise
pattern: [vertical_push]
equipment: [barbell]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 3
  mobility_prerequisite: 2

muscles:
  - id: deltoid_anterior
    role: primary
  - id: deltoid_lateral
    role: primary
  - id: triceps_brachii
    role: primary
  - id: rectus_femoris
    role: secondary
  - id: vastus_lateralis
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: erector_spinae
    role: secondary
  - id: external_oblique
    role: secondary
  - id: gluteus_maximus
    role: secondary

# ebd_2026 literature compilation. All activation data qualitative or comparative only.
# Power output data (75% and 65% 1RM) is quantitative but represents mechanical output,
# not %MVIC. Preserved as condition notes.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      phase: full_rep
      comparison: "push press vs strict overhead press"
    measurements:
      - {muscle: erector_spinae,    mean_pct_mvc: null, notes: "Significantly greater than strict overhead press (p<0.05); driven by dynamic deceleration-acceleration load transfer"}
      - {muscle: external_oblique,  mean_pct_mvc: null, notes: "Elevated to stabilize spine against dynamic loading; significantly greater than strict press (p<0.05)"}
      - {muscle: rectus_femoris,    mean_pct_mvc: null, notes: "Heavily active during eccentric dip and concentric drive phases"}
      - {muscle: vastus_lateralis,   mean_pct_mvc: null, notes: "Heavily active during eccentric dip and concentric drive phases"}
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      notes: "Power output optimization conditions"
    measurements:
      - {muscle: deltoid_anterior, mean_pct_mvc: null, notes: "Peak upper body power at 75% 1RM; mean upper body power at 65% 1RM"}

joint_rom_required:
  knee_flexion_deg: null
  shoulder_flexion_deg: 180
  notes: >
    Knee flexion restricted to a shallow quarter-squat (~10–15% of lifter height).
    Torso must remain vertical during the dip to prevent forward bar drift.
    Terminal overhead position requires full shoulder flexion (180°) with locked elbows.
  source: "ebd_2026"

strength_curve:
  type: accommodated
  sticking_point: terminal_lockout
  peak_force_position: dip_to_drive_transition
  notes: >
    Lower body kinetic energy transfer bypasses the strict overhead press sticking point
    at chin-to-eye level. Peak mechanical demand occurs at the transition from eccentric
    dip to concentric drive. The sticking point shifts to terminal lockout where the
    triceps must lock out the loaded bar at high velocity.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: moderate
    lower_back: moderate
    knee: low
  common_injuries:
    - structure: shoulder_subacromial_space
      mechanism: impingement_at_overhead_lockout
      risk_factors: [forward_head_posture, inadequate_thoracic_extension, bar_drifting_forward]
    - structure: lumbar_disc
      mechanism: dynamic_compression_from_dip_and_drive
      risk_factors: [forward_torso_lean_during_dip, inadequate_core_bracing, heavy_loads]
  contraindications:
    - acute_shoulder_impingement
    - acute_lumbar_disc_herniation
    - shoulder_labral_pathology

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

# Push Press

The push press is a barbell overhead pressing exercise that incorporates a lower-body "dip and drive" to transfer power through the kinetic chain and assist the arms in pressing heavy loads overhead. Unlike the strict overhead press, the push press is a full-body movement. The brief lower-body dip generates kinetic energy that carries the bar past the strict press sticking point at chin-to-eye level, allowing loads 15–25% heavier than the strict press max to be taken overhead.

## Execution

1. Begin in the front rack position: bar across the anterior deltoids and clavicle, elbows at 45°, grip just outside shoulder width
2. Inhale and brace hard; perform a rapid, shallow dip — bend the knees to approximately a quarter squat while keeping the torso vertical
3. At the bottom of the dip, immediately reverse direction in an explosive triple extension of the hips, knees, and ankles
4. The lower body drive accelerates the bar; once momentum carries it to forehead level, press through to full lockout with elbows straight, bar over the crown of the head
5. Lower the bar back to the front rack under control; do not drop it

## What the Data Shows

The available data from ebd_2026 is comparative, not absolute, but establishes the push press's unique muscular profile relative to the strict overhead press.

**Erector spinae and external oblique**: Both are significantly more active in the push press than the strict overhead press (p < 0.05). The explosive dip-and-drive creates a rapid acceleration/deceleration cycle that demands far greater spinal stabilization than the slow grind of a strict press. This is why the push press is used to develop core stiffness in strength and power athletes — not just shoulder strength.

**Lower body**: The rectus femoris, vastus lateralis, and biceps femoris are heavily recruited during both the eccentric dip (controlling the descent) and the concentric drive. The push press is a compound exercise with meaningful lower-body demand — it is not simply a shoulder press with a leg assist.

**Power output**: Peak upper body mechanical power is maximized at 75% of 1RM; mean power is maximized at 65% 1RM. These intensities are the practical optimal zone for push press training when power development (rather than maximal strength) is the goal.

## The Bypassed Sticking Point

The strict overhead press has a severe sticking point at chin-to-eye level where the anterior deltoids reach their weakest mechanical position. The push press bypasses this zone entirely via kinetic energy transfer — the bar arrives at the trouble zone already traveling upward at high velocity, eliminating the need to generate force in the weakest portion. The sticking point shifts to terminal lockout, where the triceps must stabilize and lock the bar at the end of an accelerated movement.

This is why the push press can produce 15–25% greater load than the strict press: it doesn't eliminate the shoulder demand, it reroutes force production through a mechanically superior range.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Strict overhead press | No lower body; full shoulder demand | Maximum shoulder strength development |
| Push jerk | Re-bend after drive; lower bar catch | Greater load capacity; Olympic lifting derivative |
| Dumbbell push press | Independent arms | Bilateral asymmetry assessment; shoulder rehabilitation |

> For system-specific training applications, see each system's lens entry.
