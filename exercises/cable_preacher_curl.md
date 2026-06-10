---
id: cable_preacher_curl
name: Cable Preacher Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [cable, preacher_bench]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary
  - id: brachioradialis
    role: secondary

# No peer-reviewed EMG data found specifically for the cable preacher curl.
# Mechanically similar to barbell preacher curl but with constant tension via cable at the bottom.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 116
  shoulder_flexion_deg: 50
  source: "biomechanical inference from preacher_curl"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Cable provides constant tension at bottom of range where free-weight preacher has near-zero load — the ascending curve of the barbell preacher is converted to more bell-shaped by the cable"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, heavy_load]
  contraindications:
    - acute_distal_biceps_tendinopathy

variations: []
progressions: []
alternatives: [preacher_curl, barbell_curl]

sources: []
---

# Cable Preacher Curl

The cable preacher curl combines the arm-bracing isolation of the preacher bench with the constant-tension load profile of a cable. Unlike the barbell preacher curl — where the resistance is near zero at full elbow extension due to gravity alignment — the cable maintains tension throughout the entire range, including at the bottom where the biceps is at its longest and most injury-susceptible position.

## Execution

1. Place a preacher bench 2–3 feet in front of a low cable pulley; attach a straight bar or EZ-bar attachment
2. Sit at the bench with the upper arms resting flat against the pad; the cable should run directly up the pad's slope
3. Starting at full extension (cable taut), curl the bar to shoulder height
4. Lower under control; do not allow the weight stack to pull the elbow into hyperextension

## Cable vs Barbell Preacher: The Critical Difference

The barbell preacher curl has an **ascending strength curve** — resistance is greatest at the bottom where the elbow is extended. This means the sticking point is at the most stretched position, and momentum-driven cheating can allow the bar to drop freely to the bottom (where the distal biceps tendon is most at risk).

The cable preacher converts this to a more **bell-shaped curve** because the cable provides constant tension even at full elbow extension. Benefits:
1. The biceps is loaded under tension at the most vulnerable lengthened position rather than having zero load there
2. This controlled eccentric at full stretch reduces the "crashing" risk present with free-weight preacher curls
3. Continuous tension from the cable eliminates the "dead zone" at the bottom of the barbell version

## Best Use Case

The cable preacher curl is particularly appropriate for:
- Trainees with a history of distal biceps tendon issues who want to train the preacher pattern with controlled bottom-range loading
- High-volume biceps work where constant tension reduces joint stress accumulation
- As a companion to barbell preacher curls to provide a different resistance profile for the same joint angle

> For system-specific training applications, see each system's lens entry.
