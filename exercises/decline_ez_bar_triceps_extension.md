---
id: decline_ez_bar_triceps_extension
name: Decline EZ-Bar Triceps Extension
status: complete
category: exercise
pattern: [isolation]
equipment: [ez_bar, bench]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary

muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: 15
    population: "healthy female volunteers, 20-24 yr"
    condition:
      load_pct_1rm: null
      implement: "barbell"
      phase: dynamic
      notes: "Tested as flat 'lying barbell extensions' (skull crusher); decline variant not specifically measured. Values are relative to triangle push-up = 100%, NOT true %MVIC. Long head 70% (SD 20.9), lateral head 55% (SD 14.1) of reference."
    measurements:
      - muscle: triceps_long
        mean_pct_mvc: null
        sd: null
      - muscle: triceps_lateral
        mean_pct_mvc: null
        sd: null
      - muscle: triceps_medial
        mean_pct_mvc: null
        sd: null

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_extension_deg: 10
  source: "biomechanical inference"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped similar to flat skullcrusher; decline angle shifts gravity moment arm distribution slightly"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: moderate
    shoulder: low
  common_injuries:
    - structure: distal_triceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, heavy_load, bouncing_at_bottom]
  contraindications:
    - acute_triceps_tendinopathy
    - blood_pressure_contraindicated_for_inverted_positions

variations: []
progressions: []
alternatives: [ez_bar_skullcrusher, lying_triceps_press]

sources:
  - title: "ACE-sponsored research: Best triceps exercises"
    author: "Boehler, B. et al."
    year: 2011
    doi: null
    source_id: boehler_2011
    credibility: practitioner
---

# Decline EZ-Bar Triceps Extension

The decline EZ-bar triceps extension is performed on a decline bench with the feet secured, performing elbow extension against the EZ-bar's load. The decline angle (typically 15–30°) creates a shoulder position in slight extension, which places the triceps long head in a slightly more elongated position than the flat skullcrusher while still performing the same elbow extension movement pattern.

## Execution

1. Secure the feet at the high end of a decline bench; lie back with the head at the lower end
2. Hold the EZ-bar with close grip, arms extended perpendicular to the torso
3. Lower the bar by bending only the elbows, allowing the bar to approach the forehead
4. Extend the elbows to return; keep the upper arms stationary throughout

## Mechanical Difference from Flat Skullcrusher

On a flat bench, the shoulder is at approximately 90° flexion when the arms are extended overhead. On a decline bench:
- The legs are elevated, tilting the body so the head is lower than the hips
- In the arms-extended starting position, the shoulders are in slight extension relative to the torso axis
- This extends the long head's proximal length slightly beyond the flat variation

The practical effect is a modest increase in long head tension through the range. The decline extension is primarily useful for lifters who find the decline position more comfortable for their elbows or who want a slight variation in stimulus.

## Safety Note

The inverted position of a decline bench slightly increases intracranial pressure. Trainees with blood pressure conditions should consult a physician before using decline variations. Use a spotter for the bar due to the awkward loading position.

> For system-specific training applications, see each system's lens entry.
