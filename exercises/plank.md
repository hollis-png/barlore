---
id: plank
name: Plank
status: complete
category: exercise
pattern: [isolation]
equipment: [bodyweight]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: rectus_abdominis
    role: primary
  - id: external_oblique
    role: primary
  - id: internal_oblique
    role: secondary
  - id: transverse_abdominis
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: multifidus
    role: stabilizer

# McGill 2010 literature review values; forearm plank sustained hold.
# Values reported as %MVC (maximum voluntary contraction) — treat as equivalent
# to %MVIC for indexing. No single DOI for forearm plank; these represent
# averages across McGill's laboratory studies compiled in the 2010 review.
muscle_activation_studies:
  - source_id: mcgill_2010
    doi: "10.1519/SSC.0b013e3181df4521"
    n: null
    population: "mixed cohorts, laboratory compilation"
    condition:
      position: forearm_plank
      phase: sustained_isometric
    measurements:
      - {muscle: rectus_abdominis, mean_pct_mvc: 50.0, sd: null}
      - {muscle: external_oblique, mean_pct_mvc: 49.0, sd: null}
      - {muscle: erector_spinae,   mean_pct_mvc: 35.0, sd: null}

joint_rom_required:
  notes: "Static isometric hold; no dynamic ROM threshold. Requires the ability to maintain lumbar neutral in a prone-supported position. Ankle plantarflexion needed for toes-only contact point."
  source: "McGill 2010"

strength_curve:
  type: isometric
  sticking_point: null
  peak_force_position: null
  notes: "No dynamic force curve — the plank is a timed static hold. Difficulty scales with lever arm length (elevating feet, raising one limb) or duration, not with load."
  source: "McGill 2010"

injury_risk:
  joint_stress:
    lumbar: low
    shoulder: low
  common_injuries:
    - structure: lumbar_spine
      mechanism: extension_under_compressive_load
      risk_factors: [sagging_hips, breath_holding_increasing_intra_abdominal_pressure, exceeding_duration_before_technique_breaks]
    - structure: glenohumeral_joint
      mechanism: impingement
      risk_factors: [internal_rotation_of_shoulder_during_elbow_plank, excessive_duration_with_protracted_scapulae]
  contraindications:
    - acute_lumbar_disc_herniation

variations: []
progressions: []
alternatives: [dead_bug]

sources:
  - source_id: mcgill_2010
    title: "Core Training: Evidence Translating to Better Performance and Injury Prevention"
    author: "McGill, S. M."
    year: 2010
    doi: "10.1519/SSC.0b013e3181df4521"
    credibility: literature_review
---

# Plank

The plank is an isometric anti-extension core exercise performed in a prone-supported position on the forearms and toes. The goal is to resist lumbar extension and maintain a rigid, straight line from heels to crown. It is the foundational movement for anti-extension core training and a prerequisite for more demanding progressions.

## Execution

1. Place the forearms flat on the floor, elbows directly below the shoulders, forearms parallel or hands clasped
2. Extend the legs back, supporting only on the toes; feet hip-width apart
3. Brace the entire midsection — contract the glutes, squeeze the quads, and create tension through the torso
4. Align the body from heels to ears in a single plane; do not let the hips sag or pike up
5. Breathe steadily; do not hold the breath, which dramatically increases spinal compressive load
6. Hold the position; terminate the set when lumbar neutral cannot be maintained

## What the EMG Data Shows

McGill's laboratory work shows the forearm plank produces moderate bilateral activation across the core musculature: rectus abdominis (~50% MVC), external oblique (~49% MVC), and lumbar erector spinae (~35% MVC). These values are lower than many dynamic exercises but are produced simultaneously and held continuously — the cumulative spinal stability demand is the training stimulus, not peak activation.

The transverse abdominis and multifidus contribute to segmental stiffness but are not captured by surface EMG in these studies; their contribution is inferred from spinal stability models.

## Common Faults and Corrections

| Fault | Effect | Fix |
|-------|--------|-----|
| Hips sagging | Lumbar hyperextension; compressive stress | Drive hips up until the body is flat; squeeze glutes harder |
| Hips piked up | Reduces core demand; becomes a shoulder exercise | Lower hips until heels, hips, and shoulders are level |
| Breath holding | Spikes intra-abdominal pressure; increases lumbar compression | Breathe slowly throughout the hold |
| Protracted scapulae | Shoulder impingement risk | Depress and slightly retract the shoulder blades; "pull shoulders away from ears" |

## Progressions

The plank is not made harder by simply holding longer — once 60 seconds can be maintained with perfect form, progression should increase the mechanical demand:

1. **Feet-elevated plank** — elevating the feet increases the lever arm and shifts more load anteriorly
2. **Single-arm or single-leg plank** — reduces the base of support, creating rotational demand
3. **RKC (Hardstyle) Plank** — maximal full-body co-contraction superimposed on the hold; dramatically increases core activation at shorter durations
4. **Ab Wheel Rollout** — transforms the anti-extension demand from static to dynamic

> For system-specific training applications, see each system's lens entry.
